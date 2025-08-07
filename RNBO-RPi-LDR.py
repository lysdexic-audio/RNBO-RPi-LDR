from gpiozero import LightSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from pythonosc import udp_client
import time

# send all OSC messages to port 1234 via loopback address
client = udp_client.SimpleUDPClient("127.0.0.1", 1234)

# start the transport via OSC
client.send_message("/rnbo/jack/transport/rolling", 1)

# read the sensor from GPIO pin 4
sensor = LightSensor(4, pin_factory=PiGPIOFactory())

try:
    while True:
        light_level = sensor.value
        print(light_level)
        client.send_message(
            "/rnbo/inst/0/params/cutoff/normalized", light_level)
        # sleep briefly to avoid unnecessary work
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Exiting...")
    sensor.close()
