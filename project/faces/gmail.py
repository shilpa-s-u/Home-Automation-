
import smtplib 
#import ssl
#import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import password
password = password.password

reciever = 'ajayshankar17.bp@gmail.com'
sender = ' sanmathid922@gmail.com'

msg = MIMEMultipart()
msg['To'] = reciever 
msg['From'] = 'realmeX' + '<' + sender + '>'
msg['Subject']= 'image testing'


msg_ready = MIMEText('trying to send the image through python.','plain')

image_open = open('user1.jpg','rb').read()
image_ready = MIMEImage(image_open,'jpg',name='test+++test.jpg')

msg.attach(msg_ready)
msg.attach(image_ready)

server =  smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender, password)
print("logged in")
server.sendmail(sender, reciever, msg.as_string())
print("successfully sent mail!!")
server.quit()
#context_data = ssl.create_default_context()

#with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context_data) as +++mail:
    
 #   mail.login(sender, password)
    
  #  smtplib.send_message(msg)    
