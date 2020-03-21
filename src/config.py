import network
import time
from machine import Pin, SPI

import bme280
import max44009
import epaper2in7


ESSID = "your_essid"
PASSWORD = "your_password"
MQTT_SERVER = "10.3.141.1"

TOPIC_TEMPERATURE = "home/weather_station/temperature"
TOPIC_PRESSURE = "home/weather_station/pressure"
TOPIC_HUMIDITY = "home/weather_station/humidity"
TOPIC_ILLUMINANCE = "home/weather_station/illuminance"

SDA_PIN = 27
SCL_PIN = 14

SCREEN_W = 176
SCREEN_H = 264


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    while not wlan.isconnected():

        print("connecting to network...")
        wlan.connect(ESSID, PASSWORD)

        time.sleep(5)

    print("network config:", wlan.ifconfig())


def mqtt_is_connected(mqtt_client):
    try:
        mqtt_client.ping()
        mqtt_client.ping()
    except:
        print("Lost connection to mqtt broker...")
        return False
    else:
        return True


def setup_sensors(i2c):

    while True:
        try:
            bme = bme280.BME280(i2c=i2c)
            light_sensor = max44009.MAX44009(i2c)
            break
        except Exception as e:
            print("One sensor couldn't be initialized: {}".format(e))
            time.sleep(3)
            continue

    print("Sensors ready")

    return bme, light_sensor


def setup_screen():
    # SPIV on ESP32
    sck = Pin(18)
    miso = Pin(19)  # Not physically connected
    mosi = Pin(23)
    dc = Pin(22)
    cs = Pin(5)
    rst = Pin(21)
    busy = Pin(4)
    spi = SPI(2, baudrate=100_000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

    screen = epaper2in7.EPD(spi, cs, dc, rst, busy)
    screen.init()

    print("Screen ready")

    return screen
