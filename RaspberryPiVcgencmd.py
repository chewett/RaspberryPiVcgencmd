import subprocess

class RaspberryPiVcgencmd:

    def get_cpu_temp(self, fahrenheit=False):
        lines = subprocess.check_output(["vcgencmd", "measure_temp"])
        temp = float(self._parse_lines(lines)['temp'][:-2])

        if fahrenheit:
            temp = ((temp * 9.0)/5.0) + 32

        return temp

    def get_ram_split(self):
        lines_arm = subprocess.check_output(["vcgencmd", "get_mem", "arm"])
        lines_gpu = subprocess.check_output(["vcgencmd", "get_mem", "gpu"])
        arm = self._parse_lines(lines_arm)['arm']
        gpu = self._parse_lines(lines_gpu)['gpu']
        return {
            "arm": arm,
            "gpu": gpu
        }

    def measure_volts(self, type="core"):
        if type in ["core", "sdram_c", "sdram_i", "sdram_p"]:
            lines = subprocess.check_output(["vcgencmd", "measure_volts", type])
            data = self._parse_lines(lines)
            return float(data['volt'][:-1])
        else:
            raise ValueError("Type must be one of core, sdram_c, sdram_i, sdram_p")

    def is_codec_available(self, codec):
        if codec in ["H264", "MPG2", "WVC1", "MPG4", "MJPG", "WMV9"]:
            line = subprocess.check_output(["line", "codec_enabled", codec])
            return self._parse_line_get_value(line)
        else:
            raise ValueError("Codec must be one of H264, MPG2, WVC1, MPG4, MJPG, WMV9")

    def _parse_line_get_value(self, line):
        return line.split("=")[1]

    def _parse_lines(self, lines):
        split_lines = lines.split("\n")
        dict_response = {}
        for line in split_lines:
            equal_split = line.split("=")
            if len(equal_split) == 2:
                dict_response[equal_split[0]] = equal_split[1]


        return dict_response
