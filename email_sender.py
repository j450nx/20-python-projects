# go over to our gmail account and setup 2-factor authentication
# generate app password
# create a function to send the mail

from email.message import EmailMessage
from app_password import password
import ssl
import smtplib

email_sender = '709394x@gmail.com'
email_password = password
# https://temp-mail.org/en/ to generate a temporary email
email_receiver = 'cidit61489@lubde.com'

subject = "2022, Dec, 12"
body = """
Greetings. Happy holidays.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())