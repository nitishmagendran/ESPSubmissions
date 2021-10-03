# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import network
from machine import Pin
from time import sleep
led = Pin(2,Pin.OUT)
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
ap_name = "realme X"
password = "Lightning"
while not sta_if.isconnected():
    sta_if.connect(ap_name, password ) # Connect to an AP

if sta_if.isconnected():
    led.value(1)
    sleep(1)
    led.value(0)
import webrepl
webrepl.start()
