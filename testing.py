import RPi.GPIO as GPIO
# import GPIO
import time

GPIO.setmode(GPIO.BCM)

DAC = [12, 13, 18, 19]
GPIO.setup(DAC, GPIO.OUT)

GPIO.output(13, GPIO.HIGH)
time.sleep(1)
GPIO.output(13, GPIO.LOW)
time.sleep(1)
GPIO.output(12, GPIO.HIGH)
time.sleep(1)
GPIO.output(12, GPIO.LOW)
time.sleep(1)
GPIO.output(19, GPIO.HIGH)
time.sleep(1)
GPIO.output(19, GPIO.LOW)
time.sleep(1)
GPIO.output(18, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
