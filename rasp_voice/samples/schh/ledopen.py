import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
# while True:
GPIO.output(23,True)
#     time.sleep(1)
#     GPIO.output(24,False)
#     time.sleep(1)
# GPIO.cleanup()
