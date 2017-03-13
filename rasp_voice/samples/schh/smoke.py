import RPi.GPIO as GPIO
import time
# GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel, GPIO.IN)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24,False)
time.sleep(1)

while(1):
    GPIO.setmode(GPIO.BCM)
    channel = 17
    GPIO.setup(channel, GPIO.IN)
    GPIO.setup(24,GPIO.OUT)
    while GPIO.input(channel) == GPIO.HIGH:
        GPIO.output(24,True)

        continue
    while GPIO.input(channel) == GPIO.LOW:
        GPIO.output(24,False)
        time.sleep(0.02005)   #led per second 
        continue
    GPIO.cleanup()
GPIO.cleanup()

#dc-5V out-GPIO4 GND-GND led-gpio24
