#!/usr/bin/env python

from bottle import Bottle
import json

app = Bottle()

def get_data():
  with open("temp.txt", "r") as f:
    try:
      return json.load(f)
    except:
      return {"humidity": None, "temperature": None}

print(get_data())

@app.get('/')
def index():
    return dict(get_data())

# For prometheus
@app.get('/metrics')
def metrics():
  data = get_data()
  if data['temperature'] != None:
    return "# TYPE temperature gauge\ntemperature %f\n# TYPE humidity gauge\nhumidity %f\n" % (data['temperature'], data['humidity'])

app.run(host='0.0.0.0', port=8081)
