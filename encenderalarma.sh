
#!/bin/bash
# -*- coding: utf-8 -*-

msg="Se ha detectado movimiento!! Vigila lo que está pasando en: http://www.ustream.tv/channel/dqEMu9XW2pz"

python /home/pi/alarma_camara.py &  # Encender alarma


/home/pi/enviarmensaje.sh TEW "$msg" & #Enviar mensaje
