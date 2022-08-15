# Write your code here :-)
from microbit import *

def graph(analog_reading):

    display.clear() #Clears the display so that LEDs that aren't supposed to be on are turned off.
    stops = 0
    stops = analog_reading/40.92 # 40.92 is 1023/25, which is the increments for each graphing

    for y in range(4, -1, -1): #Has to be negative because it will start at 4, and then stop at 0.
        for x in range(5):
            if stops > 0:
                display.set_pixel(x,y,9) #Sets the pixel in for each in row y, and then it goes up. Allows for convenience when viewing
                stops-=1
            else:
                return  #Once out of increments, it exits function so that it doesn't do a full screen each time.



while True:
    value = pin1.read_analog()

    graph(value)

    if button_a.is_pressed():
        display.scroll(value)

    sleep(50)
