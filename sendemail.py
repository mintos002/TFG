#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import sys #Para obtener args
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

RPIEMAIL="raspberrytfg@gmail.com"
#TOEMAIL="raspberrytfg@gmail.com"
TOEMAIL="mintos002@gmail.com"
PASSWORD="RaspberryTFGPassw0rd"

def main():
	if len(sys.argv)==1:
		print 'Se necesitan argumentos. ej. python sendemail.py "Mensaje" "PATH del archivo adjunto (opcional)"'
		return False

	MESSAGE=str(sys.argv[1])

	msg = MIMEMultipart()

	msg['From'] = RPIEMAIL
	msg['To'] = TOEMAIL
	msg['Subject'] = "Alarma!"

	body = MESSAGE

	msg.attach(MIMEText(body, 'plain'))

	if len(sys.argv)==3:
		FILEPATH=str(sys.argv[2])	#Obtener segundo argumento
		fns=FILEPATH.split('/')		#Separar el string por '/'
		filename=fns[len(fns)-1]	#Obtener nombre del archivo

		attachment = open(FILEPATH, "rb")

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

		msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(RPIEMAIL, PASSWORD)
	text = msg.as_string()
	server.sendmail(RPIEMAIL, TOEMAIL, text)
	server.quit()

	print "Se ha enviado un email a: "+TOEMAIL

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Se ha cancelado el envio"
