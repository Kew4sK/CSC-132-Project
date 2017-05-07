########################################################
# Name: Pete Mace
# Date: 5/7/17
# Description: RPi Final Project Button Sequence
########################################################
import RPi.GPIO as GPIo
import pygame

#the switches and LEDs from left to right
switches = [18, 23, 12, 21]
leds = [5, 6, 19, 26]

#use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the input and output pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

seq = [0, 1, 2, 3]


# we'll discuss this later, but this allows us to detect
# when Ctrl+C is pressed so that we can reset the GPIO pins
# keep going until the user presses Ctrl+C
while (True):
        # wait for player input (via the switches)
        # initialize the count of switches pressed to 0
        count = 0
        # keep accepting player input until the number of items in the sequence is reached
        while (count < len(seq)):
                # initially note that no switch is pressed
                # this will help with switch debouncing
                pressed = False
                # so long as no switch is currently pressed...
                while (not pressed):
                        # ...we can check the status of each switch
                        for i in range(len(switches)):
                                # if one switch is pressed
                                while (GPIO.input(switches[i]) == True):
                                        # note its index
                                        val = i
                                        # note that a switch has now been pressed
                                        # so that we don't detect any more switch presses
                                        pressed = True


                # light the matching LED
                GPIO.output(leds[val], True)
                # wait and turn the LED off again
                sleep(1)
                GPIO.output(leds[val], False)
                sleep(0.25)

                # check to see if this LED is correct in the sequence
                if (val != seq[count]):
                        # player is incorrect; invoke the lose function
                        lose()
                        print "Succesful failure!"
                        # reset the GPIO pins
                        GPIO.cleanup()
                        # exit the game
                        exit(0)
                print "Good Job! You did it!"

