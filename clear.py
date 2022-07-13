import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

DAC = [12, 13, 18, 19]
GPIO.setup(DAC, GPIO.OUT)

GPIO.output(DAC, GPIO.LOW)