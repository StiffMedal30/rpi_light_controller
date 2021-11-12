import serial
import time
from flask import Flask, redirect

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()
    



@app.route('/light/on')
def lights_on():
    print("request on")
    line = serialComsWrite(b"on\n")
    print(line)
    return redirect('/')


@app.route("/light/off")
def lights_off():
    print("request off")
    line = serialComsWrite(b"off\n")
    return redirect('/')


@app.route("/light/status")
def light_status():
    line = serialComsRead(b"status\n")
    if line == "":
        line = "unknown"
    
    print("status:" + line)
    
    return redirect("/")


@app.route("/")
def lights():
    return "hello"


def serialComsWrite(state):
    ser = serial.Serial('/dev/ttyAMA0',9600 , timeout=1)
    ser.flush()
    ser.write(state)
    time.sleep(0.5)
    line = ser.readline().decode('utf-8').rstrip()
    return line

def serialComsRead(state):
    ser = serial.Serial('/dev/ttyAMA0',9600 , timeout=1)
    ser.flush()
    ser.write(state)
    time.sleep(0.5)
    line = ser.readline().decode('utf-8').rstrip()
    return line


