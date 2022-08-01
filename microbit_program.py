# Add your Python code here. E.g.
from microbit import *
while True:
    if display.read_light_level() < 100:
        display.show(Image.HAPPY)
    if display.read_light_level() > 100:
        display.show(Image.SAD)