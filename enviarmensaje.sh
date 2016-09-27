#!/bin/bash
# -*- coding: utf-8 -*-
wn=34687644952 #NUM telefono
tn="Alex_Juan" #Contacto telegram
modo=$1;
msg=$2;


if [[ -z $msg ]] || [[ -z $modo ]] #Si el mensage está vacio o no tiene modo
then
   echo 'Ejemplo de uso: ./enviarmensaje.sh WTE "Hola mundo"'
   echo 'Modos soportados:'
   echo 'W --> WhatsApp'
   echo 'T --> Telegram'
   echo 'E --> e-mail'
   echo 'e --> imagen por email'
   echo 't --> imagen por tg'
else

   if [[ $modo == *"t"* ]] #Si el modo es t
   then
     /home/pi/tg_photo.sh $tn "$msg" & #se envia la foto
   fi
   if [[ $modo == *"e"* ]] # si el modo es e
   then
      python /home/pi/sendemail.py "Imagen adjunta" "$msg" & #Se envia imagen 
   fi
   if [[ $modo == *"W"* ]] #Si modo contiene W envia un mensaje por WhatsApp
   then
      sudo /home/pi/yowsup/yowsup-cli demos -c /home/pi/yowsup/mydetails  -s $wn "$msg" &  # Enviar mensaje por WhatsApp
   fi
   if [[ $modo == *"T"* ]] #Si modo contiene "T" envia un mensaje por Telegram
   then
      /home/pi/tg_msg.sh $tn "$msg" &  # Enviar mensaje por Telegram
   fi
   if [[ $modo == *"E"* ]] #Si modo contiene "E" envia un mensaje por e-mail
   then
      python /home/pi/sendemail.py "$msg" &  #Enviar email
   fi
fi
