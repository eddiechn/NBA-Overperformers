import os 
from datetime import datetime, timedelta
from email.message import EmailMessage
import ssl
import smtplib
import subprocess
import pandas as pd
from diff_rankings import results



now = datetime.now()
yesterday = now - timedelta(days=1)
formatted_yesterday = yesterday.strftime('%B %d, %Y')

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")



subject = f"NBA Overperformers for {formatted_yesterday}"
body = results()

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body, subtype = "html")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp: 
    smtp.login(email_sender, email_password)
    smtp.send_message(em)

