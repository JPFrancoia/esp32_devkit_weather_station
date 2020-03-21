import machine
import time
import framebuf
from umqtt.robust import MQTTClient

import config
import pics
from writer import Writer, NotionalDisplay
import freesans20


i2c = machine.I2C(scl=machine.Pin(config.SCL_PIN), sda=machine.Pin(config.SDA_PIN))
mqtt_client = MQTTClient("umqtt_client", config.MQTT_SERVER)
bme, max44009 = config.setup_sensors(i2c)
screen = config.setup_screen()

config.do_connect()

buf = bytearray(config.SCREEN_W * config.SCREEN_H // 8)
fb = framebuf.FrameBuffer(buf, config.SCREEN_W, config.SCREEN_H, framebuf.MONO_HLSB)

black = 1
white = 0

fb.fill(white)
fb.blit(pics.fb_thermometer, 0, 2)
fb.blit(pics.fb_humidity, 0, 62)
fb.blit(pics.fb_pressure, 0, 122)
fb.blit(pics.fb_light, 0, 182)

screen.display_frame(buf)


my_display = NotionalDisplay(176, 264, buf)
writer = Writer(my_display, freesans20)


while True:

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

    fb.fill(white)
    fb.blit(pics.fb_thermometer, 0, 2)
    fb.blit(pics.fb_humidity, 0, 62)
    fb.blit(pics.fb_pressure, 0, 122)
    fb.blit(pics.fb_light, 0, 182)

    Writer.set_textpos(my_display, 25, 70)
    writer.printstring("{} C".format(round(float(temperature), 2)))

    Writer.set_textpos(my_display, 85, 65)
    writer.printstring("{} hPa".format(round(float(pressure), 2)))

    Writer.set_textpos(my_display, 145, 70)
    writer.printstring("{} %".format(round(float(humidity), 2)))

    Writer.set_textpos(my_display, 205, 70)
    writer.printstring("{} Lux".format(round(float(illuminance), 2)))

    my_display.show()
    screen.display_frame(buf)

    time.sleep(10)
