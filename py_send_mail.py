from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'jacob.gallegos.c@gmail.com'
email_password = password
email_receiver = ''

subject = "Don't forget to subscribe"
body = """
  If you watch a video, please share, hit the like button and subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 456, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())