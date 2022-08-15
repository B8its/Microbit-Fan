# Write your code here :-)
from microbit import *

def shock():
    a = accelerometer.get_values()
    for i in range(len(a)):
        if abs(a[i])>2039 and i != 1:
            display.scroll("Dropped", 50)

while True:
    shock()

