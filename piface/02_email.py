# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
textfile = 'exemplo.txt'
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
#msg = MIMEText(fp.read())
msg = MIMEText('Teste Email Python')
#fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Teste Email %s' % textfile
msg['From'] = 'miguel.espregueira@cerealis.pt'
msg['To'] = 'div-ti@cerealis.pt'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('192.168.1.90')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
