from RaspberryPiVcgencmd import RaspberryPiVcgencmd

sen = RaspberryPiVcgencmd()

print sen.get_cpu_temp(), "'C"
print sen.get_cpu_temp(fahrenheit=True), "'F"

print "Ram split", sen.get_ram_split()

print "Core voltage", sen.measure_volts()
print "sdram_c voltage", sen.measure_volts("sdram_c")
print "sdram_i voltage", sen.measure_volts("sdram_i")
print "sdram_p voltage", sen.measure_volts("sdram_p")

print "H264 available", sen.is_codec_available("H264")
print "MPG2 available", sen.is_codec_available("MPG2")
print "WVC1 available", sen.is_codec_available("WVC1")
print "MPG4 available", sen.is_codec_available("MPG4")
print "MJPG available", sen.is_codec_available("MJPG")
print "WMV9 available", sen.is_codec_available("WMV9")

