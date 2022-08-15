from microbit import *

def adjust(analog_temp):
    temp = 0
    temp = 0.10775978189420144*analog_temp-29.42990164
    temp = round(temp)
    return temp
"""
The results from excel into a scatter graph.
Using a linear trendline. The formula comes from excel.
-9.2799x = 286.35-y
9.7299x = y-286.35
x = 0.10775978189420144-29.42990164
"""


def graph(analog_reading): # This function is used to graph the analog reading the screen.

    display.clear() #Clears the display so that LEDs that aren't supposed to be on are turned off.
    stops = 0
    stops = analog_reading/40.92 # 40.92 is 1023/25, which is the increments for each graphing

    for y in range(4, -1, -1): #Does a for loop going down. This is because the y0 on the Mbit is at the top.
        for x in range(5):
            if stops > 0:
                display.set_pixel(x,y,9) #Sets the pixel in for each in row y, and then it goes up. Allows for convenience when viewing
                stops-=1
            else:
                return  #Once out of increments, it exits function so that it doesn't do a full screen each time.

def main():
    on=True
    real_temp = 0
    while on:
        analog_temp = pin1.read_analog()

        real_temp = adjust(analog_temp)

        graph(analog_temp) #Graphs the analog reading onto the screen


        if button_a.is_pressed():
            display.scroll(real_temp) #If button is pressed, then display the analog reading. This will allow calibration.
        elif button_b.is_pressed():
            display.scroll(analog_temp)
        sleep(50) #This is needed otherwise the screen will be flashing frantically.

if __name__ == "__main__":
    main()
