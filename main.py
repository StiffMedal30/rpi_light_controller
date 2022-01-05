import serial
import time
import requests
from flask import Flask, redirect, jsonify, url_for


app = Flask(__name__)
URL = 'http://christiaan.ddns.net'


if __name__ == '__main__':
    app.debug = True
    app.run()




@app.route('/light/on')
def lights_on():
    serialComs(b"on\n")
    return ""


@app.route("/light/off")
def lights_off():
    serialComs(b"off\n")
    return ""


@app.route("/light/status")
def light_status():
    status = serialComs(b"status\n")
    print(status)
    if status == "":
        status = "unknown"
    if status == "n":
        status = "on"
    if status == "f":
        status = "off"
    return lights(status)


@app.route("/")
def lights(status):
    return status




def serialComs(state):
    ser = serial.Serial('/dev/ttyAMA0',9600 , timeout=1)
    ser.flush()
    ser.write(state)
    time.sleep(0.5)
    line = ser.readline().decode('utf-8').rstrip()
    return line
