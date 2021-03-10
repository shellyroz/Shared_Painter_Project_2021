import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "shellyscyberproject@gmail.com"
password = "CYB5RpA1nT5r"
send_to_email = "shellyscyberproject@gmail.com"
# send_to_email = "sherry.r0zman@gmail.com"

subject = "Trying Something For My Project"
message = "HEY! How's it going? :)"

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
