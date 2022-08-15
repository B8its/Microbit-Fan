from microbit import *

def errorCheck(value, lastValue):
    if abs(value-lastValue) > 100:
        display.scroll("eu")

    elif value > 750 or value < 200:
        display.scroll("eo")


value = pin1.read_analog()
toggle = True
while True:

    lastValue = value
    if toggle:
        if button_a.is_pressed() and button_b.is_pressed():
            toggle = False
            display.scroll("m")
        value = pin1.read_analog()
    else:
        if button_a.is_pressed() and button_b.is_pressed():
            toggle = True
            display.scroll("a")

        elif button_a.is_pressed():
            value+=20
            display.scroll(value)

        elif button_b.is_pressed():
            value-=20
            display.scroll(value)

    print(value)
    errorCheck(value, lastValue)
    sleep(100)
