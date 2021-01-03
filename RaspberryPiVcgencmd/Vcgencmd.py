import subprocess

__author__ = "Christopher Hewett <chewett@hotmail.co.uk>"

class Vcgencmd:
    """
        Helper function to get information in a python way out of the vcgencmd Raspberry Pi executable
    """

    def __init__(self):
        # TODO: add a "vcgencmd run" check and first time its called we should check what commands are supported
        # TODO: allow specifying where vcgencmd lives.
        pass

    def get_cpu_temp(self, fahrenheit=False):
        """Get the cpu temperature of the soc, optionally request output in fahrenheit"""
        lines = subprocess.check_output(["vcgencmd", "measure_temp"])
        temp = float(self._parse_lines(lines)['temp'][:-2])

        if fahrenheit:
            temp = ((temp * 9.0)/5.0) + 32

        return temp

    def get_ram_split(self):
        """Get the ram split between cpu/gpu this returns a dict"""

        lines_arm = subprocess.check_output(["vcgencmd", "get_mem", "arm"])
        lines_gpu = subprocess.check_output(["vcgencmd", "get_mem", "gpu"])
        arm = self._parse_lines(lines_arm)['arm']
        gpu = self._parse_lines(lines_gpu)['gpu']
        return {
            "arm": arm,
            "gpu": gpu
        }

    def measure_volts(self, type="core"):
        """Measures the volts on parts of the chip"""

        if type in ["core", "sdram_c", "sdram_i", "sdram_p"]:
            lines = subprocess.check_output(["vcgencmd", "measure_volts", type])
            data = self._parse_lines(lines)
            return float(data['volt'][:-1])
        else:
            raise ValueError("Type must be one of core, sdram_c, sdram_i, sdram_p")

    def measure_clock(self, type):
        """Returns the clock speed in Hz of various parts of the chip"""
        if type in ["arm", "core", "h264", "isp", "v3d", "uart", "pwm", "emmc", "pixel", "vec", "hdmi", "dpi"]:
            line = subprocess.check_output(["vcgencmd", "measure_clock", type])
            return self._parse_line_get_value(line)
        else:
            raise ValueError("Type must be on of arm, core, h264, isp, v3d, uart, pwm, emmc, pixel, vec, hdmi, dpi")

    def is_codec_available(self, codec):
        """Returns whether the codec is available on the Raspberry Pi"""
        if codec in ["H264", "MPG2", "WVC1", "MPG4", "MJPG", "WMV9"]:
            line = subprocess.check_output(["vcgencmd", "codec_enabled", codec])
            return (self._parse_line_get_value(line) == "enabled")
        else:
            raise ValueError("Codec must be one of H264, MPG2, WVC1, MPG4, MJPG, WMV9")

    def get_version(self):
        """Gets the version string of the firmware"""
        return subprocess.check_output(["vcgencmd", "version"]).decode("utf-8").rstrip()

    def set_display_power(self, power):
        """Sets the display power of the Raspberry Pi, warning setting this to 0 will disable video output"""
        if power in [0, 1]:
            subprocess.check_output(["vcgencmd", "display_power", str(power)])
        else:
            raise ValueError("Power must be either 0 or 1")

    def _parse_line_get_value(self, line):
        """Helper function to get the output from vcgencmd and parse it"""
        return line.decode("utf-8").split("=")[1].rstrip()

    def _parse_lines(self, lines):
        """Helper function to parse multiline output"""
        split_lines = lines.decode("utf-8").split("\n")
        dict_response = {}
        for line in split_lines:
            equal_split = line.split("=")
            if len(equal_split) == 2:
                dict_response[equal_split[0]] = equal_split[1]

        return dict_response
