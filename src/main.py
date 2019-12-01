import machine
import time
from umqtt.robust import MQTTClient

import bme280

import max44009
import config

i2c = machine.I2C(scl=machine.Pin(config.SCL_PIN), sda=machine.Pin(config.SDA_PIN))

c = MQTTClient("umqtt_client", config.MQTT_SERVER)

bme = bme280.BME280(i2c=i2c)
max44009 = max44009.MAX44009(i2c)

while True:
    print(bme.values)
    print(max44009.illuminance_lux)

    temperature = bme.values[0].replace("C", "")
    pressure = bme.values[1].replace("hPa", "")
    humidity = bme.values[2].replace("%", "")
    illuminance = str(max44009.illuminance_lux)

    c.connect()

    c.publish(config.TOPIC_TEMPERATURE, temperature, qos=1)
    c.publish(config.TOPIC_PRESSURE, pressure, qos=1)
    c.publish(config.TOPIC_HUMIDITY, humidity, qos=1)
    c.publish(config.TOPIC_ILLUMINANCE, illuminance, qos=1)

    c.disconnect()

    time.sleep(5)
