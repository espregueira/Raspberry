
def enviaemail(strAssunto, strCorpo, strDe='miguel.espregueira@cerealis.pt', strPara='div-ti@cerealis.pt')

	# Import smtplib for the actual sending function
	import smtplib

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


