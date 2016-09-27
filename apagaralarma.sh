#!/bin/bash
msg="Alarma desactivada"

sudo kill -9 $(ps aux | grep '[p]ython /home/pi/alarma_camara.py' | awk '{print $2}')  #Busca el proceso y lo interrumpe
python /home/pi/CleanUp.py

/home/pi/enviarmensaje.sh TEW "$msg" &  #Enviar mensaje

