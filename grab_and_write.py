#!/usr/bin/env python3

import MyPyDHT
from json import dumps

try:
  humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT11, 22, reading_attempts = 35)
  print(dumps({"humidity": humidity, "temperature": temperature}))
except:
  1 + 1
