from microbit import *



def shock():
    a = accelerometer.get_values()
    for i in range(len(a)):
        if abs(a[i])>2039 and i != 1:
            pin0.write_analog(0)
            raise Exception("The Microbit has fallen or received significant shock, restart microbit to turn it back on")

"""   ^^^
This function will be called each loop to check if the microbit has received sudden shock,
such as being knocked or falling
"""

def adjust(analog_temp):
    temp = 0
    temp = 0.10775978189420144*analog_temp-29.42990164
    temp = round(temp)
    return temp
""" ^^^^
The results from excel into a scatter graph.
Using a linear trendline. The formula comes from excel.
-9.2799x = 286.35-y
9.7299x = y-286.35
x = 0.10775978189420144-29.42990164
"""

def calculateMotorSpeed(bottom, top):
    bottom = max(0, bottom)
    percent = min(bottom/top, 1) * 1023
    stage = int(percent/(1020/3.5))
    return percent, stage

"""
Using percentage calculations, we can easily set the motor speed without the need of If statements
This makes the code much cleaner and faster.
The formula is :
(x/y)*z
Where x = value
y = max value
z = multiplier

"""

def showLEDS(stage):

    pins = ["16", "9", "8"]

    for i in range(3):
        if stage > 0:
            eval("pin"+pins[i]+".write_digital(1)")
            stage -= 1 # I forgot to add this line
        else:
            eval("pin"+pins[i]+".write_digital(0)")

""" ^^^
This function is used to show the leds in terms of power.
If the power is over a certain threshold, then it will turn on LEDS in a series
This works by using a list, containing a string of the pin numbers that are being used
and getting how many leds should be on as an input.
Then using a for loop, it scrolls through the loop the required times
In the loop, is an if else statement, with the stage.
If the stage is greater than 0
then using an eval function, it will call the function to set the digital output of a pin to 1
Else, it will use the eval function to call a function to set the digital output of a pin to 0
"""

def graph(reading, maximum): # This function is used to graph the analog reading the screen.

    display.clear() #Clears the display so that LEDs that aren't supposed to be on are turned off.
    stops = 0
    stops = reading / maximum / 25

    for y in range(4, -1, -1): #Does a for loop going down. This is because the y0 on the Mbit is at the top.
        for x in range(5):
            if stops > 0:
                display.set_pixel(x,y,9) #Sets the pixel in for each in row y, and then it goes up. Allows for convenience when viewing
                stops-=1
            else:
                return  #Once out of increments, it exits function so that it doesn't do a full screen each time.

""" ^^^
This Function is used to graph to the screen.
It uses a double for loop to go through each x and y.
"""

def errorCheck(value, lastValue):
    if abs(value-lastValue) > 100:
        pin0.write_analog(0)
        raise Exception("Error with temperature sensor. ")

    elif value > 700 or value < 200:
        pin0.write_analog(0)
        raise Exception("Error with temperature sensor. ")

"""
This Function is used to check whether the values that we get from the temperature sensor are correct.
This works by making sure the variation between the last value and the current value
and making sure that it doesn't look like noise. it also checks if the value is somehow extremely high, which means something is wrong.
"""


def main():
    analog_reading = pin1.read_analog()
    on = False
    max_temp = 30

    while True:

            last_reading = analog_reading
            analog_reading = pin1.read_analog()

            errorCheck(analog_reading, last_reading)

            current_temp = adjust(analog_reading)

            speed, stage = calculateMotorSpeed(current_temp-20, max_temp-20)

            if button_a.is_pressed():
                display.scroll(current_temp)


            showLEDS(stage)
            pin0.write_analog(speed)
            sleep(100)


if __name__ == "__main__":
    main()
