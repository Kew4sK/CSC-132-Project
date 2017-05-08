import RPi.GPIO as GPIO
from time import sleep
import pygame

switches = [18, 23, 12, 21]
leds = [5, 6, 19, 26]

GPIO.setmode(GPIO.BCM)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(leds, GPIO.OUT)

a = False
b = False
c = False
d = False

while (True):
    input_state1 = GPIO.input(18)
    input_state2 = GPIO.input(23)
    input_state3 = GPIO.input(12)
    input_state4 = GPIO.input(21)
    if (input_state1 == True):
        a = True
        if (input_state2 == True):
            b = True
            if (input_state3 == True):
                c = True
                if (input_state4 == True):
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
