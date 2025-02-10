import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

def send_email_to_user(semail,password,remail,subject,body):
    sender_email=semail
    password=password

    resever_email=remail 

    message=MIMEMultipart()
    message['From']=sender_email
    message['To']=resever_email
    message['Subject']=subject


    message.attach(MIMEText(body,'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(sender_email,password)
            server.sendmail(sender_email,resever_email,message.as_string())
        print("Email is successfully sent")
    except smtplib.SMTPAuthenticationError as e:
        print("SMTP Authentication Error:", e)
