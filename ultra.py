from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
from ultrasonic import Ultrasonic

ultrasonic_sensor = Ultrasonic()
initialize()
clear_oled()

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    add_text(0, 0, str(int(distance_value)))




