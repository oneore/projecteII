import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        os.system('python reconeix_sum_copy.py')
    input_state2 = GPIO.input(24)
    if input_state2 == False:
        os.system('python clear.py')
