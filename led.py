import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Led:
    def __init__(self, port, name):
        self.port = port        
        self.name = name
        GPIO.setup(self.port,GPIO.OUT)

    def on(self):
        GPIO.output(self.port,GPIO.HIGH)

    def off(self):
        GPIO.output(self.port,GPIO.LOW)

    def __str__(self) -> str:
        return "Colour: " + self.name
