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
## Posting a json payload

The headers really need to be passed, urequests doesn't seem to guess it's
posting json.

```python
headers = {'Content-Type': 'application/json'}
r = urequests.post("http://192.168.0.101:5000/measurements/provide", json={"measurement": 1}, headers=headers)
```
