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

#Set switches from left to right
switches = [26, 19, 21, 20, 16, 12, 25, 24, 23, 18]

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
        input_state0 = GPIO.input(26)
        input_state1 = GPIO.input(19)
        input_state2 = GPIO.input(21)
        input_state3 = GPIO.input(20)
        input_state4 = GPIO.input(16)
        input_state5 = GPIO.input(12)
        input_state6 = GPIO.input(25)
        input_state7 = GPIO.input(24)
        input_state8 = GPIO.input(23)
        input_state9 = GPIO.input(18)
        #if the button is pressed the variable becomes true
        if (input_state9 | a):
            a = True
            if (input_state0 | b):
                b = True
                if (input_state8 | c):
                    c = True
                    if (input_state2 | d):
                        d = True
                        if (input_state1 | e):
                            e = True
                            if (input_state7 | f):
                                f = True
                                if (input_state4 | g):
                                    g = True
                                    if (input_state3 | h):
                                        h = True
                                        if (h == True):
                                            print "Succesful Code Entry!"
                                            break
except:
    GPIO.cleanup()
