#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

# Variables globales:
CAMLED = 32     # pin externo a la raspberry (LED de la camara)
BEEP = 17       # pin 17 en BCM

# Usar numeracion GPIO
def setup():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(BEEP, GPIO.OUT, initial=GPIO.HIGH)

if __name__ == "__main__":
   setup()
   GPIO.cleanup()
