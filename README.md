Raspberry Pi Vcgencmd
=============================

A small python library to programmatically access some of the internal
sensors of the Raspberry Pi

## Usage

Add the module into your git repository as a submodule and then commit it

```
git submodule add https://github.com/chewett/RaspberryPiVcgencmd
git commit
```

Include the module in your python file

`from RaspberryPiVcgencmd.RaspberryPiVcgencmd import RaspberryPiVcgencmd`

Once you have included it you can use it in your program as below

```
vcgencmd = RaspberryPiVcgencmd()
print vcgencmd.get_version()
```

## Exposed Functions

The majority of the useful output from vcgencmd is exposed in the class with the below functions

* get_cpu_temp - Gets the system temperature of the soc in Celsius or Fahrenheit
* get_ram_split - Gets the memory split between the gpu and cpu
* measure_volts - Measures the voltage of various internal components
* measure_clock - Mesures the clock frequency of various internal components
* is_codec_available - Returns whether the codec specificed video/audio codec is available on the Raspberry Pi
* get_version - Gets the version of the firmware installed on the Raspberry Pi
* set_display_power - Allows turning off/on the video output of the Raspberry Pi

## Todo

* The first time vcgencmd is requested to run it should run
and then check what commands are available on that Raspberry Pi.
This should then confirm that the command is available and also
stop any commands which are not available on the Pi.
* Combine some of the output functions so that it doesnt use several
different formatting methods

## Want to help?

Suggestions and improvements are welcome, if you have anything to add
feel free to make a pull request on github
