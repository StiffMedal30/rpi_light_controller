import RPi.GPIO as GPIO
import serial
from flask import Flask, redirect

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()
    



relay = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)



@app.route('/light/on')
def lights_on():
    line = serialComs(b"on\n")
    return redirect('/' + str(line))


@app.route("/light/off")
def lights_off():
    line = serialComs(b"off\n")
    return redirect('/' + str(line))


@app.route("/<line>")
def lights(line):
    print("The Light Is Now " + line)
    return str(line)

def serialComs(state):
    ser = serial.Serial('/dev/ttyACM0',9600 , timeout=1)
    ser.flush()
    ser.write(state)
    line = ser.readline().decode('utf-8').rstrip()
    return line


