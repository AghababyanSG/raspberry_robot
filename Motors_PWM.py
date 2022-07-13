import RPi.GPIO as GPIO
import time

GPIO_PWM_0 = 12
GPIO_PWM_1 = 13
WORK_TIME = 2
DUTY_CYCLE = 20
FREQUENCY = 100

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_PWM_0, GPIO.OUT)
GPIO.setup(GPIO_PWM_1, GPIO.OUT)

pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)
pwmOutput_1 = GPIO.PWM(GPIO_PWM_1, 2 * FREQUENCY)

pwmOutput_0.start(DUTY_CYCLE)
#pwmOutput_1.start(DUTY_CYCLE)

time.sleep(5)

DUTY_CYCLE=50
pwmOutput_0.start(DUTY_CYCLE)
time.sleep(WORK_TIME)

DUTY_CYCLE=70
pwmOutput_0.start(DUTY_CYCLE)
time.sleep(WORK_TIME)

DUTY_CYCLE=100
pwmOutput_0.start(DUTY_CYCLE)
time.sleep(WORK_TIME)
pwmOutput_0.stop()
#pwmOutput_1.stop()
GPIO.cleanup()