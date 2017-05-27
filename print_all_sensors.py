from RpiInternalSensors import RpiInternalSensors

sen = RpiInternalSensors()

print sen.get_cpu_temp(), "'C"
print sen.get_cpu_temp(fahrenheit=True), "'F"
print sen.get_ram_split()
