import imghdr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

email = "shellyscyberproject@gmail.com"
password = "CYB5RpA1nT5r"
# send_to_email = "shellyscyberproject@gmail.com"
send_to_email = "sherry.r0zman@gmail.com"

subject = "Trying Something For My Project"
message = "HEY! How's it going? :)"

#msg = MIMEMultipart()
# msg['From'] = email
# msg['To'] = send_to_email
# msg['Subject'] = subject

'''IMAGE'''

msg = EmailMessage()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

with open("smiley_png.png", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
