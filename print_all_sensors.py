from RpiInternalSensors import RpiInternalSensors

sen = RpiInternalSensors()

print sen.get_cpu_temp()
print sen.get_ram_split()
