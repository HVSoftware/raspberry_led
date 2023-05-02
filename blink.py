import time

class Blink:
    def __init__(self, led) -> None:
        self.led = led

    def blink(self, times, interval):    
        i = 0
        self.led.on()
        time.sleep(interval)
        while i < times:
            self.led.off()    
            time.sleep(interval)            
            self.led.on()    
            time.sleep(interval)
            i += 1
        self.led.off()    

    def __str__(self) -> str:
        return "Blink: " + self.led + " " + self.times + " " + self.interval 