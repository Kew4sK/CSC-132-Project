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
switches = [18, 23, 24, 25, 12, 16, 20, 21, 19, 26]
leds = [17, 22, 5, 6, 13]

#set 
GPIO.setmode(GPIO.BCM)

#set inputs
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#These variables form the toggle mode of each switch
a = False
b = False
c = False
d = False
e = False
f = False
g = False
h = False


try:    
    while (True):
        #sets each button as an input state
        input_state0 = GPIO.input(18)
        input_state1 = GPIO.input(23)
        input_state2 = GPIO.input(24)
        input_state3 = GPIO.input(25)
        input_state4 = GPIO.input(12)
        input_state5 = GPIO.input(16)
        input_state6 = GPIO.input(20)
        input_state7 = GPIO.input(21)
        input_state8 = GPIO.input(19)
        input_state9 = GPIO.input(26)
        #if the button is pressed the variable becomes true
        if (input_state0 | a):
            a = True
            if (input_state1 | b):
                b = True
                if (input_state2 | c):
                    c = True
                    if (input_state3 | d):
                        d = True
                        if (input_state4 | e):
                            e = True
                            if (input_state5 | f):
                                f = True
                                if (input_state6 | g):
                                    g = True
                                    if (input_state7 | h):
                                        h = True
                                        if (h == True):
                                            print "Succesful Code Entry!"
                                            break
except:
    GPIO.cleanup()
