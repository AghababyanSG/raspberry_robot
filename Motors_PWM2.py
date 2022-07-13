import RPi.GPIO as GPIO
import time

GPIO_PWM_0 = 12
GPIO_PWM_1 = 13
GPIO_PWM_L0 = 18
GPIO_PWM_L1 = 19
#WORK_TIME = 2

FREQUENCY = 490

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_PWM_0, GPIO.OUT)
GPIO.setup(GPIO_PWM_1, GPIO.OUT)
GPIO.setup(GPIO_PWM_L0, GPIO.OUT)
GPIO.setup(GPIO_PWM_L1, GPIO.OUT)

def Start_Motors(forward, Right, Left, Time):
    if forward=='forward':
        pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)
        GPIO.output(GPIO_PWM_1, 0)
        pwmOutput_1 = GPIO.PWM(GPIO_PWM_L0, FREQUENCY)
        GPIO.output(GPIO_PWM_L1, 0)
        pwmOutput_0.start(Right)
        pwmOutput_1.start(Left)
        time.sleep(Time)
        pwmOutput_0.stop(Right)
        pwmOutput_1.stop(Left)
        time.sleep(0)
        GPIO.cleanup()
    elif forward=='back':
        pwmOutput_0 = GPIO.PWM(GPIO_PWM_1, FREQUENCY)
        pwmOutput_1 = GPIO.PWM(GPIO_PWM_L1, FREQUENCY)
        GPIO.output(GPIO_PWM_L0, 0)
        GPIO.output(GPIO_PWM_0, 0)
        pwmOutput_0.start(Right)
        pwmOutput_1.start(Left)
        time.sleep(Time)
        pwmOutput_0.stop(Right)
        pwmOutput_1.stop(Left)
#pwmOutput_1.start(DUTY_CYCLE)
'''
Start_Motors("forward", 100, 100, 2)
time.sleep(0)
GPIO.cleanup()'''