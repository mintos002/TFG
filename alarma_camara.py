#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import pygame

# Variables globales:
CAMLED = 32	# pin externo a la raspberry (LED de la camara)
BEEP = 17	# pin 17 en BCM

# Usar numeracion GPIO
def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(CAMLED, GPIO.OUT, initial=False)
	GPIO.setup(BEEP, GPIO.OUT, initial=GPIO.HIGH)

def dispararLedCamara():
	print '...Alarma disparada'
	# Iluminar el led de la camara	
	for i in range(5):
		GPIO.output(CAMLED, True)	# LED on
		time.sleep(0.5)
		GPIO.output(CAMLED, False)	# LED off
		time.sleep(0.5)
	GPIO.output(CAMLED, False)

def dispararArchivoAudio():
	# Reproducir el sonido de alarma
	pygame.mixer.init()
        pygame.mixer.music.load("myalarm.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

def dispararBeep():
	# Activar el beep
	#print 'Activando beep'
	for i in range(20):
		GPIO.output(BEEP, GPIO.LOW)
		time.sleep(0.2)
		GPIO.output(BEEP, GPIO.HIGH)
		time.sleep(0.1)
	GPIO.output(BEEP, GPIO.HIGH)

if __name__ == '__main__':	# Ejecutar los metodos que se desee
	setup()
	try:
		while True : 
			dispararBeep()
#		dispararLedCamara()
#		dispararArchivoAudio()
	except KeyboardInterrupt:
		print 'Alarma interrumpida...'
	except :
		print 'Error inesperado'
	finally:
		GPIO.cleanup() # Asegura limpiar los pines al finalizar el script
