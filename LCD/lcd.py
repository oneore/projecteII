from RPLCD.gpio import CharLCD
from RPi import GPIO
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[2, 16, 4, 15])
lcd.write_string(u'Hello world!')
