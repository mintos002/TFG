# -*- coding: utf-8 -*-
import os, subprocess, time
import RPi.GPIO as GPIO

from yowsup.layers.interface                           import YowInterfaceLayer	                #Reply to the message
from yowsup.layers.interface                           import ProtocolEntityCallback            #Reply to the message
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity	        #Body message
from yowsup.layers.protocol_presence.protocolentities  import AvailablePresenceProtocolEntity   #Online
from yowsup.layers.protocol_presence.protocolentities  import UnavailablePresenceProtocolEntity #Offline
from yowsup.layers.protocol_presence.protocolentities  import PresenceProtocolEntity            #Name presence
from yowsup.layers.protocol_chatstate.protocolentities import OutgoingChatstateProtocolEntity   #is writing, writing pause
from yowsup.common.tools                               import Jid                               #is writing, writing pause

#Log, but only creates the file and writes only if you kill by hand from the console (CTRL + C)
#import sys
#class Logger(object):
#    def __init__(self, filename="Default.log"):
#        self.terminal = sys.stdout
#        self.log = open(filename, "a")
#
#    def write(self, message):
#        self.terminal.write(message)
#        self.log.write(message)
#sys.stdout = Logger("/1.txt")
#print "Hello world !" # this is should be saved in yourlogfilename.txt
#------------#------------#------------#------------#------------#------------

allowedPersons=['34687644952'] #Filtro de numeros permitidos
ap = set(allowedPersons)

name = "NAMEPRESENCE"
filelog = "/root/.yowsup/Not allowed.log"

# Methods
def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BEEP, GPIO.OUT, initial=GPIO.HIGH)
	print 'Inside setup'

def sendImage():
        print "Enviando una imagen"
        

# Set GPIOs
BEEP = 17 # pin 17 en BCM

# Clear pins and start setup
GPIO.cleanup()
setup()

class EchoLayer(YowInterfaceLayer):
    # Avisar que se ha iniciado
    print 'CMD via WhatsApp iniciado'

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            time.sleep(0.5)
            self.toLower(messageProtocolEntity.ack()) #Set received (double v)
            time.sleep(0.5)
            self.toLower(PresenceProtocolEntity(name = name)) #Set name Presence
            time.sleep(0.5)
            self.toLower(AvailablePresenceProtocolEntity()) #Set online
            time.sleep(0.5)
            self.toLower(messageProtocolEntity.ack(True)) #Set read (double v blue)
            time.sleep(0.5)
            self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_TYPING, Jid.normalize(messageProtocolEntity.getFrom(False)) )) #Set is writing
            time.sleep(2)
            self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_PAUSED, Jid.normalize(messageProtocolEntity.getFrom(False)) )) #Set no is writing
            time.sleep(1)
            self.onTextMessage(messageProtocolEntity) #Send the answer
            time.sleep(3)
            self.toLower(UnavailablePresenceProtocolEntity()) #Set offline

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        print entity.ack()
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        namemitt   = messageProtocolEntity.getNotify()
        message    = messageProtocolEntity.getBody().lower()
        recipient  = messageProtocolEntity.getFrom()
        textmsg    = TextMessageProtocolEntity

        #For a break to use the character \n
        #The sleep you write so #time.sleep(1)

        if messageProtocolEntity.getFrom(False) in ap:
            print "He recibido: "+message
            if message == 'hi' or message == 'hola':
                answer = "Hola "+namemitt+" " 
                self.toLower(textmsg(answer, to = recipient ))
                print answer
              
            elif message == 'help'or message == 'ayuda':
                answer = "Hola "+namemitt+", los comandos validos són:\n\nTemperatura\nEspacio\nReiniciar pi\nApagar pi\nGPIO17 on\nGPIO17 off\nLimpiar gpio\nEncender camara\nApagar camara\nPara otros comandos: $/(comando)"
                self.toLower(textmsg(answer, to = recipient ))
                print answer

            elif message == 'temperatura' or message == 'temperature':
                t=float(subprocess.check_output(["/opt/vc/bin/vcgencmd measure_temp | cut -c6-9"], shell=True)[:-1])
                ts=str(t)
                answer = 'Mi temperatura es: '+ts+' °C'
                self.toLower(textmsg(answer, to = recipient ))
                print answer

            elif message == 'Espacio' or message == 'disk':
                result=subprocess.check_output("df -h .", shell=True)
                output=result.split()
                answer = "Espacio del disco:\nTotal: "+output[8]+"\nUsado: "+output[9]+" ("+output[11]+")\nLibre: "+output[10]
                self.toLower(textmsg(answer, to = recipient ))
                #print answer

            elif message == 'reboot pi' or message == 'reiniciar pi':
                answer = "Ok "+namemitt+", reiniciando... Hasta luego."
                self.toLower(textmsg(answer, to = recipient ))
                print answer
                time.sleep(3)
                self.toLower(UnavailablePresenceProtocolEntity())
                time.sleep(2)
                os.system('sudo reboot')

	    elif message == 'shutdown pi' or message == 'apagar pi':
		answer = "Ok, "+namemitt+", apagando... Bye Bye."
		self.toLower(textmsg(answer, to = recipient ))
		print answer
		time.sleep(3)
		self.toLower(UnavailablePresenceProtocolEntity())
		time.sleep(2)
		os.system('sudo shutdown -h now')

            elif message == 'gpio17 off':
                GPIO.output(17, True) # Pin 2 in up
                answer = "Ok, GPIO17 puesto a True"
                self.toLower(textmsg(answer, to = recipient ))
                print answer

            elif message == 'gpio17 on':
                GPIO.output(17, False) # Pin 2 in down
                answer = "Ok, GPIO17 puesto a False"
                self.toLower(textmsg(answer, to = recipient ))
                print answer

	    elif message == 'cleanup gpio' or message == 'limpiar gpio':
		GPIO.cleanup()
		answer = "GPIO limpios"
		self.toLower(textmsg(answer, to = recipient ))

            elif message == 'encender camara' or message == 'camera on' or message == 'activar camara':
                print "Activando camara..."
                subprocess.call("/home/pi/runall.sh", shell=True)
                self.toLower(textmsg("Se ha activado la camara", to = recipient ))
                print "Camara activada"

            elif message == 'apagar camara' or message == 'camera off' or message == 'desactivar camara':
                print "Desactivando camara..."
                subprocess.call("/home/pi/killall.sh", shell=True)
                self.toLower(textmsg("Se ha desactivado la camara", to = recipient ))
                print "Camara desactivada"

            elif message[:2] == '$/':
                result=subprocess.check_output(message[2:], shell=True)
                answer = "Respuesta:  "+result+" "
                self.toLower(textmsg(answer, to = recipient ))

            elif message == 'akan':
                answer = "Kan de jan"
                self.toLower(textmsg(answer, to = recipient ))

	    # Si no reconoce el mensaje:
            else:
                answer = "Lo siento "+namemitt+", no entiendo el comando: "+message+" ..." 
                self.toLower(textmsg(answer, to = recipient))
                print answer

        else:
            answer = "Hola "+namemitt+", lo siento, pero no puedo conectarme contigo..."
            time.sleep(20)
            self.toLower(textmsg(answer, to = recipient))
            print answer
            out_file = open(filelog,"a")
            out_file.write("------------------------"+"\n"+"Sender:"+"\n"+namemitt+"\n"+"Number sender:"+"\n"+recipient+"\n"+"Message text:"+"\n"+message+"\n"+"------------------------"+"\n"+"\n")
            out_file.close()
