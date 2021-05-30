# Name: Shelly Rozman
# Python Version: 3.7.2
# Date: 14/3/2021

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import imghdr
from random import randint

class EmailBot:
    def __init__(self):
        self.my_email = "shellyscyberproject@gmail.com"
        self.my_password = "CYB5RpA1nT5r"
        self.code_email_subject = "SHARED PAINTER - Your Login Code"
        self.code_email_message = "Hi! Your login code is: "
        self.code_msg = MIMEMultipart()
        self.screenshot_email_subject = "SHARED PAINTER - Your Painting"
        # self.screenshot_email_message = "Thank you for using Shared Painter! Here is your painting :) "
        self.screenshot_msg = EmailMessage()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.code = ""

    def create_login_code(self):
        '''
        The function creates a login code by generating random numbers.
        :return: The created login code/
        :rtype: string.
        '''
        login_code = ""

        for i in range(6):
            login_code += str(randint(0, 9))

        return login_code

    def compose_code_email_message(self):
        '''
        The function composes an email message with a login code.
        :return: An email message with a login code.
        :rtype: string.
        '''
        self.code = self.create_login_code()
        self.code_email_message += self.code
        return self.code_email_message


    def send_code_email(self, send_to_email):
        '''
        The function sends an email containing a login code to the given email address.
        :param send_to_email: A given email address.
        :return:
        '''
        self.code_msg['From'] = self.my_email
        self.code_msg['To'] = send_to_email
        self.code_msg['Subject'] = self.code_email_subject

        self.server = smtplib.SMTP('smtp.gmail.com', 587)

        self.code_msg.attach(MIMEText(self.compose_code_email_message(), 'plain'))

        self.server.starttls()
        self.server.login(self.my_email, self.my_password)

        text = self.code_msg.as_string()
        self.server.sendmail(self.my_email, send_to_email, text)

        del self.screenshot_msg['From']
        del self.code_msg['To']
        del self.code_msg['Subject']
        self.server.quit()


    def send_screenshot_email(self, send_to_email, screenshot_path):
        '''
        The function sends an email containing a login code to the given email address.
        :param send_to_email: A given email address.
        :return:
        '''
        self.screenshot_msg['From'] = self.my_email
        self.screenshot_msg['To'] = send_to_email
        self.screenshot_msg['Subject'] = self.screenshot_email_subject

        self.server = smtplib.SMTP('smtp.gmail.com', 587)

        print("PATH:", screenshot_path)

        with open(screenshot_path, "rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        print("NAME:", file_name)

        self.screenshot_msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

        screenshot_email_message = "Thank you for using Shared Painter! Here is your painting :) "

        self.screenshot_msg.attach(MIMEText(screenshot_email_message, 'plain'))

        self.server.starttls()
        self.server.login(self.my_email, self.my_password)

        #text = self.screenshot_msg.as_string()
        #self.server.sendmail(self.my_email, send_to_email, text)

        self.server.send_message(self.screenshot_msg)

        del self.screenshot_msg['From']
        del self.screenshot_msg['To']
        del self.screenshot_msg['Subject']
        self.screenshot_msg.clear()
        self.server.quit()



#c = EmailBot()

#c.send_code_email("sherry.r0zman@gmail.com")
#c.send_screenshot_email("sherry.r0zman@gmail.com", "Cropped_Screenshots\Cherrys_cropped_screenshot.png")

