import os
import serial
from dotenv import load_dotenv

load_dotenv('.env')

serial_arduino = serial.Serial(os.getenv('ARDUINO_PORT'), 9600)

while True:
    number = input("Give me a number: ")
    serial_arduino.write(number.encode('ascii'))
