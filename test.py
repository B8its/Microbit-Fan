# Write your code here :-)
from microbit import *

while True:
    a = pin0.read_analog()
    if button_a.is_pressed():
        display.scroll(a)
        #232, 148
        #579, 436

