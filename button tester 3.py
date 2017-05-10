#####################################################
#Team 3: Pete Mace, Conan Howard, Justin Turnbull
# Date: 5/9/17
# Purpose: The system that the teams will come enter 
# the code they get from the puzzle into
#####################################################

#imports libraries neccesary
import RPi.GPIO as GPIO
from time import sleep
import pygame

#Set switches and leds to pins from left to right
switches = [18, 23, 12, 21]
leds = [5, 6, 19, 26]

#set 
GPIO.setmode(GPIO.BCM)

#set inpiuts and outputs
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

#These variables form the toggle mode of each switch
a = False
b = False
c = False
d = False

#Keep the lights off from the beginning
GPIO.output(leds,False)

try:    
    while (True):
        #sets each button as an input state
        input_state1 = GPIO.input(18)
        input_state2 = GPIO.input(23)
        input_state3 = GPIO.input(12)
        input_state4 = GPIO.input(21)
        #if the button is pressed the variable becomes true
        #if the button is pressed or the variable is True, the next button becomes useful
        #If a button is messed up in the sequence then should quit
        if (input_state1 | a):
            a = True
            if (input_state2 | b):
                b = True
                if (input_state3 | c):
                    c = True
                    if (input_state4 | d):
                        d = True
                        if (d == True):
                            GPIO.output(leds, True)
                        else:
                            print "messed up at d"
                    else:
                        print"messed up at c"
                else:
                    print "messed up at b"
            else:
                print "messed up at a"
except:
    GPIO.cleanup()
