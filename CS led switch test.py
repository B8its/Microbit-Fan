# Write your code here :-)
from microbit import *

def showLEDS(stage):

    pins = ["16","9","8"]

    for i in range(3):
        if stage > 0:
            eval("pin"+pins[i]+".write_digital(1)")
            stage-=1
        else:
            eval("pin"+pins[i]+".write_digital(0)")

stage = 0
while True:
    if button_a.is_pressed() and stage > 0:
        stage-=1
        display.scroll(stage)
        showLEDS(stage)

    elif button_b.is_pressed() and stage < 3:
        stage+=1
        display.scroll(stage)
        showLEDS(stage)

