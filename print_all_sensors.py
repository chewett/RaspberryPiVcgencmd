from RaspberryPiVcgencmd import RaspberryPiVcgencmd

sen = RaspberryPiVcgencmd()

print sen.get_cpu_temp(), "'C"
print sen.get_cpu_temp(fahrenheit=True), "'F"
print "Ram split", sen.get_ram_split()
print "Core voltage", sen.measure_volts()
print "sdram_c voltage", sen.measure_volts("sdram_c")
print "sdram_i voltage", sen.measure_volts("sdram_i")
print "sdram_p voltage", sen.measure_volts("sdram_p")
