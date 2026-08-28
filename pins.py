import digitalio
from digitalio import DigitalInOut, Pull
from board import *
from adafruit_debouncer import Debouncer

#init button
button1_pin = DigitalInOut(GP22) # defaults to input
button1_pin.pull = Pull.UP      # turn on internal pull-up resistor
button1 =  Debouncer(button1_pin)

#init payload selection switch
# payload1 = GPIO4 to GND
# payload2 = GPIO5 to GND
# payload3 = GPIO10 to GND
# payload4 = GPIO11 to GND
payload1Pin = digitalio.DigitalInOut(GP4)
payload1Pin.switch_to_input(pull=digitalio.Pull.UP)
payload2Pin = digitalio.DigitalInOut(GP5)
payload2Pin.switch_to_input(pull=digitalio.Pull.UP)
payload3Pin = digitalio.DigitalInOut(GP10)
payload3Pin.switch_to_input(pull=digitalio.Pull.UP)
payload4Pin = digitalio.DigitalInOut(GP11)
payload4Pin.switch_to_input(pull=digitalio.Pull.UP)

# check GP6 for setup mode - changed from GP0 for Shrike Lite RP2040
progStatusPin = digitalio.DigitalInOut(GP6)
progStatusPin.switch_to_input(pull=digitalio.Pull.UP)
