import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


channel = 4




GPIO.setup(channel, GPIO.IN)
GPIO.setup(23,GPIO.OUT)
time.sleep(1)
while(1):
    while GPIO.input(channel) == GPIO.HIGH:
        GPIO.output(23,True)
        # time.sleep(1)
        continue
    while GPIO.input(channel) == GPIO.LOW:
        GPIO.output(23,False)
        # time.sleep(1)
        continue

GPIO.cleanup()
