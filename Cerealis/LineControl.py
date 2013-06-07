import piface.pfio as pfio
import time
# Import smtplib for the actual sending function
import smtplib


def enviaemail(strAssunto, strCorpo, strDe='miguel.espregueira@cerealis.pt', strPara='div-ti@cerealis.pt')

	# Import the email modules we'll need
	from email.mime.text import MIMEText
	msg = MIMEText(strCorpo)
	msg['Subject'] = strAssunto
	msg['From'] = strDe
	msg['To'] = strPara

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP('192.168.1.90')
	s.sendmail(msg['From'], msg['To'], msg.as_string())
	s.quit()
	return True



pfio.init()
AlertaLed = pfio.LED(7)
intStart=time.time()
intRead = -1
enviaemail('Inicio Programa %s' % time.strftime('%X %x %Z'),'Foi iniciado o programa de leitura')

while True:
	teste = pfio.digital_read(0)
	SwitchExit = pfio.digital_read(2)
	if (SwitchExit == 1)
		break
	#print (teste)
	if(intRead <> teste):
		print 'Mudança de leitura de %d para %d as %s' % (intRead,teste,time.strftime('%X %x %Z'))
		intRead = teste
		if(intRead == 1):
			AlertaLed.turn_on()
			intInicio = time.time()
			strCorpo='Linha X parou as %s' % (time.strftime('%X %x %Z'))
			strAssunto='Atença inicio de Paragem da Linha X' 
		elif(intRead == 0):
			AlertaLed.turn_off()
			elapsed = (time.time() - intInicio)
			strCorpo='Linha X Recomeçou o trabalho as %s teve parada %s' % (intRead,teste,time.strftime('%X %x %Z'),elapsed)
			strAssunto='Recomeçou o trabalho da Linha X' 
			print "Paragem demorou: ", elapsed

		enviaemail(strAssunto,strCorpo)

	time.sleep(1)

elapsed = (time.time() - intStart)
strCorpo='Recebida ordem de paragem de Programa as %s teve em funcionamento durante %s' % (intRead,teste,time.strftime('%X %x %Z'),elapsed)
strAssunto='Fim de Programa' 
print "Duração do funcionamento da aplicação: ", elapsed
enviaemail(strAssunto,strCorpo)


