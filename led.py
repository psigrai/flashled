#!/user/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)

for i in range(10):
    GPIO.output(11, 1)
    time.sleep(0.2)
    GPIO.output(11, 0)
    time.sleep(0.2)
GPIO.cleanup()
    
