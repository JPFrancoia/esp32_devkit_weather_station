import network
import time
from machine import Pin, SPI

import bme280
import max44009
from ili934 import ILI9341


ESSID = "your_essid"
PASSWORD = "your_password"
MQTT_SERVER = "10.3.141.1"

TOPIC_TEMPERATURE = "home/weather_station/temperature"
TOPIC_PRESSURE = "home/weather_station/pressure"
TOPIC_HUMIDITY = "home/weather_station/humidity"
TOPIC_ILLUMINANCE = "home/weather_station/illuminance"

SDA_PIN = 27
SCL_PIN = 14

SCREEN_W = 320
SCREEN_H = 240


def do_connect():
    network.WLAN(0).active(1)
    network.WLAN(1).active(1)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    while not wlan.isconnected():

        print("connecting to network...")
        wlan.connect(ESSID, PASSWORD)

        time.sleep(5)

    print("network config:", wlan.ifconfig())


def disconnect():
    network.WLAN(0).active(0)
    network.WLAN(1).active(0)


def mqtt_is_connected(mqtt_client):
    try:
        # Required to properly check the MQTT server is reachable
        # See: https://forum.micropython.org/viewtopic.php?f=15&t=7334
        mqtt_client.ping()
        mqtt_client.ping()
    except Exception as e:
        print("Lost connection to mqtt broker: {}".format(e))
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
    mosi = Pin(23)  # blue
    dc = Pin(22)  # green
    rst = Pin(21)  # white
    miso = Pin(19)  # light purple
    sck = Pin(18)  # CLK, yellow
    cs = Pin(5)  # orange

    spi = SPI(2, baudrate=40000000, miso=miso, mosi=mosi, sck=sck)

    screen = ILI9341(
        spi,
        cs=cs,
        dc=dc,
        rst=rst,
        w=320,
        h=240,
        r=2)

    print("Screen ready")

    return screen
