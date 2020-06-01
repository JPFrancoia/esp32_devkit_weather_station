import machine
import time
import framebuf
from umqtt.robust import MQTTClient

import config
import pics
import ili934
import tt32


i2c = machine.I2C(scl=machine.Pin(config.SCL_PIN), sda=machine.Pin(config.SDA_PIN))
mqtt_client = MQTTClient("umqtt_client", config.MQTT_SERVER)
bme, max44009 = config.setup_sensors(i2c)
light_sensor = config.setup_sensors(i2c)
screen = config.setup_screen()

screen.set_color(ili934.color565(255, 165, 0), ili934.color565(255, 255, 255))
screen.erase()
screen.set_font(tt32)

# Create an array to store the bytes for the pictures.
# We'll re-use it for all pictures. The pictures are 60x60 but an array of 60x60
# strangely doesn't work
buf = bytearray(120 * 120 // 8)

# Needed to invert SCREEN_H and SCREEN_W to use the screen in portrait mode
# Size should match the buffer above
fb = framebuf.FrameBuffer(buf, 120, 120, framebuf.MONO_HLSB)

# Turn ON the backlight of the screen
p0 = machine.Pin(2, machine.Pin.OUT)
p0.value(1)

# SCREEN_H and SCREEN_W are inverted to use the screen in portrait mode, for all
# the blittings belows

screen.set_color(ili934.color565(255, 165, 0), ili934.color565(255, 255, 255))
fb.blit(pics.fb_thermometer, 0, 0)
screen.blit(fb, 0, 16, 60, 60)

screen.set_color(ili934.color565(65, 105, 225), ili934.color565(255, 255, 255))
fb.blit(pics.fb_humidity, 0, 0)
screen.blit(fb, 0, 92, 60, 60)

screen.set_color(ili934.color565(119, 136, 153), ili934.color565(255, 255, 255))
fb.blit(pics.fb_pressure, 0, 0)
screen.blit(fb, 0, 168, 60, 60)

screen.set_color(ili934.color565(255, 215, 0), ili934.color565(255, 255, 255))
fb.blit(pics.fb_light, 0, 0)
screen.blit(fb, 0, 244, 60, 60)


while True:

    config.do_connect()

    for i in range(0, 3):
        try:
            mqtt_client.connect()
            break
        except Exception as e:
            print("MQTT failed to connect with {}, looping".format(e))
    else:
        config.do_connect()
        continue

    try:
        temperature, pressure, humidity = bme.values
        temperature = temperature.replace("C", "")
        pressure = pressure.replace("hPa", "")
        humidity = humidity.replace("%", "")
        print("Temperature, pressure, humidity:", temperature, pressure, humidity)
    except Exception as e:
        print("BME280 reading failed with: {}".format(e))

    try:
        illuminance = str(round(max44009.illuminance_lux, 2))
        print("Illuminance:", illuminance)
    except Exception as e:
        print("MAX44009 reading failed with: {}".format(e))

    try:
        mqtt_client.publish(config.TOPIC_TEMPERATURE, temperature)
        mqtt_client.publish(config.TOPIC_PRESSURE, pressure)
        mqtt_client.publish(config.TOPIC_HUMIDITY, humidity)
        mqtt_client.publish(config.TOPIC_ILLUMINANCE, illuminance)
    except Exception as e:
        print("Transferring data failed with: {}".format(e))

    mqtt_client.disconnect()

    # Temperature displayed in orange. Set here before erasing the measurements area
    screen.set_color(ili934.color565(255, 165, 0), ili934.color565(255, 255, 255))

    # Fill a rectangle only on the measurements area. This is equivalent to
    # screen.erase(), but we only erase the measurements area of the screen.
    screen.fill_rectangle(90, 0, config.SCREEN_H - 90, config.SCREEN_W)

    screen.set_pos(90, 30)
    screen.print("{} C".format(round(float(temperature), 2)))

    screen.set_color(ili934.color565(65, 105, 225), ili934.color565(255, 255, 255))
    screen.set_pos(90, 110)
    screen.print("{} %".format(round(float(humidity), 2)))

    screen.set_color(ili934.color565(119, 136, 153), ili934.color565(255, 255, 255))
    screen.set_pos(90, 185)
    screen.print("{} hPa".format(round(float(pressure), 2)))

    screen.set_color(ili934.color565(255, 215, 0), ili934.color565(255, 255, 255))
    screen.set_pos(90, 260)
    screen.print("{} Lux".format(round(float(illuminance), 2)))

    config.disconnect()

    time.sleep(60)
