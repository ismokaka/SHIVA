#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  traffic_light_LED.py
#
# Make 3 LEDs simulate an American street light
#
#  Copyright 2015  Ken Powers
#

# Import the modules used in the script
import time
import RPi.GPIO as GPIO

# Assign constants for the light GPIO pins
red_led = 18
yellow_led = 23
green_led = 24
RUNNING = True

# Configure the GPIO to BCM and set the pins to output mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

# Define a function to control the traffic light
def trafficState(red, yellow, green):
    GPIO.output(red_led, red)
    GPIO.output(yellow_led, yellow)
    GPIO.output(green_led, green)

print "Traffic Light Simulation. Press CTRL + C to quit"

# Main loop
try:
    while RUNNING:
        # Green for 13 seconds
        trafficState(0,0,1)
        time.sleep(13)
        # Yellow for 3 seconds
        trafficState(0,1,0)
        time.sleep(3)
        # Red for 10 seconds
        trafficState(1,0,0)
        time.sleep(10)

# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"

# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup()
