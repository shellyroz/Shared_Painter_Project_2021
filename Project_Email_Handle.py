import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint

class EmailBot:
    def __init__(self):
        self.my_email = "shellyscyberproject@gmail.com"
        self.my_password = "CYB5RpA1nT5r"
        self.email_subject = "SHARED PAINTER - Your Login Code"
        self.email_message = "Hi! Your login code is: "
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.code = ""

    def create_login_code(self):
        login_code = ""

        for i in range(6):
            login_code += str(randint(0, 9))

        return login_code

    def compose_email_message(self):
        self.code = self.create_login_code()
        self.email_message += self.code
        return self.email_message

    def send_email(self, send_to_email):
        self.msg['From'] = self.my_email
        self.msg['To'] = send_to_email
        self.msg['Subject'] = self.email_subject

        self.msg.attach(MIMEText(self.compose_email_message(), 'plain'))

        self.server.starttls()
        self.server.login(self.my_email, self.my_password)

        text = self.msg.as_string()
        self.server.sendmail(self.my_email, send_to_email, text)
        self.server.quit()





c = EmailBot()

c.send_email("sherry.r0zman@gmail.com")
