import time
import led
import blink

IO_GREEN = 17
IO_RED = 22
IO_YELLOW = 27
    
green = led.Led(IO_GREEN, "Green")
red = led.Led(IO_RED, "Red")
yellow = led.Led(IO_YELLOW, "Yellow")

redBlink = blink.Blink(red)
greenBlink = blink.Blink(green)

print(green)
print(red)
print(yellow)

greenBlink.blink(3, 1)
green.on()
time.sleep(2)
red.on()
time.sleep(2)
yellow.on()
time.sleep(2)
yellow.off()
time.sleep(2)
red.off()
time.sleep(2)
green.off()
redBlink.blink(3, 1)