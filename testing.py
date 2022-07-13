import RPi.GPIO as GPIO
# import GPIO
import time

GPIO.setmode(GPIO.BCM)

DAC = [12, 13, 18, 19]
GPIO.setup(DAC, GPIO.OUT)

GPIO.output(12, GPIO.HIGH)
time.sleep(3)
GPIO.output(12, GPIO.LOW)

