import RPi.GPIO as GPIO
from time import sleep
import pygame

switches = [18, 23, 12, 21]
leds = [5, 6, 19, 26]

GPIO.setmode(GPIO.BCM)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

a = False
b = False
c = False
d = False
state = 0
GPIO.output(leds,False)
try:
    
    while (True):
#        sleep(0.2)
        input_state1 = GPIO.input(18)
        input_state2 = GPIO.input(23)
        input_state3 = GPIO.input(12)
        input_state4 = GPIO.input(21)
#        print input_state1
#        print input_state2
#        print input_state3
#        print input_state4 
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
                            #GPIO.output(leds,False)
                    else:
                        print"messed up at c"
               #        GPIO.output(leds,False)
                else:
                    print "messed up at b"
             #      GPIO.output(leds,False)
            else:
                print "messed up at a"
            #   GPIO.output(leds,False)
except:
    GPIO.cleanup()
