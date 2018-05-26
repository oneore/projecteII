import RPi.GPIO as GPIO
import time
import os
from lcd import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        clear_screen()
        missatge("Escoltant...")
        os.system('python reconeix_sum.py')
