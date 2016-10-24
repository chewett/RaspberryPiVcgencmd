import subprocess

class RpiInternalSensors:

    def get_cpu_temp(self):
        lines = subprocess.check_output(["vcgencmd", "measure_temp"])
        temp = self.parse_lines(lines)['temp'][:-2]
        return temp

    def parse_lines(self, lines):
        split_lines = lines.split("\n")
        dict_response = {}
        for line in split_lines:
            equal_split = line.split("=")
            if len(equal_split) == 2:
                dict_response[equal_split[0]] = equal_split[1]


        return dict_response
