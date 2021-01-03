from RaspberryPiVcgencmd.RaspberryPiVcgencmd import RaspberryPiVcgencmd

sen = RaspberryPiVcgencmd()

print(sen.get_cpu_temp(), "'C")
print(sen.get_cpu_temp(fahrenheit=True), "'F")

print("Ram split", sen.get_ram_split())

voltages_to_test = ["core", "sdram_c", "sdram_i", "sdram_p"]
for voltage in voltages_to_test:
    print(voltage, "voltage", sen.measure_volts(voltage))

clocks_to_measure = ["arm", "core", "h264", "isp", "v3d", "uart", "pwm", "emmc", "pixel", "vec", "hdmi", "dpi"]
for clock in clocks_to_measure:
    print(clock, "speed", sen.measure_clock(clock))

codecs_to_test = ["H264", "MPG2", "WVC1", "MPG4", "MJPG", "WMV9"]
for codec in codecs_to_test:
    print(codec, "available", sen.is_codec_available(codec))

print("Version: ", sen.get_version())
