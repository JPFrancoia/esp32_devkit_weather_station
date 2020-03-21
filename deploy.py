import network
import upip
import time

ESSID = "your_essid"
PASSWORD = "your_password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

while not wlan.isconnected():

    print("connecting to network...")
    wlan.connect(ESSID, PASSWORD)

    time.sleep(2)

print("network config:", wlan.ifconfig())

upip.install("micropython-bme280")
upip.install("micropython-umqtt.simple")
upip.install("micropython-umqtt.robust")
