import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

print("LED ON")
GPIO.output(27,GPIO.HIGH)
time.sleep(2)
print("LED OFF")
GPIO.output(27,GPIO.LOW)
