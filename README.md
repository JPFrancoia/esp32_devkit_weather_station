## Drivers:

### MAX44009 light sensor

Manually downloaded from the repo, no upip version.

https://github.com/rcolistete/MicroPython_MAX44009_driver

Example:

```python
import max44009
from microbit import i2c
sensor = max44009.MAX44009(i2c)
sensor.illuminance_lux()
```

### BME280: pressure, temperature, humidity

Installed directly from upip.

https://github.com/SebastianRoll/mpy_bme280_esp8266

Example:
```python
import machine
import bme280

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

print(bme.values)
```

## TFT screen

Python driver for the screen comes from: https://github.com/jeffmer/micropython-ili9341

TFT screen is 2.2 inch TFT Display 240*320 pixels - ILI9341: https://www.tinytronics.nl/shop/en/display/tft/2.2-inch-tft-display-240*320-pixels-ili9341
