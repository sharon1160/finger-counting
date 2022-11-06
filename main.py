import serial

serial_arduino = serial.Serial("/dev/cu.usbmodem21301", 9600)

while True:
    number = input("Give me a number: ")
    serial_arduino.write(number.encode('ascii'))
