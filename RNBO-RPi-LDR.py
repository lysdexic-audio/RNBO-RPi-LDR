from gpiozero import LightSensor
import liblo as OSC
import sys, time

# send all messages to port 1234 on the local machine
try:
    target = OSC.Address(1234)
except OSC.AddressError as err:
    print(err)    
    sys.exit()

# start the transport via OSC
OSC.send(target, "/rnbo/jack/transport/rolling", 1)

# read the sensor from GPIO pin 4
sensor = LightSensor(4)

while True:
    light_level = sensor.value
    print(light_level)
    OSC.send(target, "/rnbo/inst/0/params/cutoff/normalized", light_level)
    time.sleep(0.01)