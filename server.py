#!/usr/bin/env python

from bottle import Bottle
import MyPyDHT

app = Bottle()

last_data = {}

def get_data():
  try:
    humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT11, 25)
    global last_data
    last_data = {'humidity': humidity, 'temperature': temperature}
    return last_data
  except:
    print("Got error grabbing sensor data")
  finally:
    return last_data 

get_data()

@app.get('/')
def index():
    return dict(get_data())

app.run(host='0.0.0.0', port=8081)
