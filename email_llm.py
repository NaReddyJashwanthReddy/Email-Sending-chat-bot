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

body='''
Dear Ravi,

We acknowledge receipt of your resignation letter dated [insert date], informing us of your decision to leave your position as [insert position] with the company, effective [insert last working day].

We understand that this decision was not made lightly, and we appreciate the contributions you have made during your time with us.

As we move forward with the transition process, please ensure the following steps are completed:
1. Return all company property, including your ID card, laptop, and any other company materials, to the HR department by your last working day.
2. Complete the exit interview, which will be scheduled by HR shortly.
3. Ensure a smooth handover of your responsibilities to your team.

If you have any questions or require assistance during this transition, please do not hesitate to reach out to the HR team.

Thank you once again for your service, and we wish you the very best in your future endeavors.

Best regards,
[Your Name]
[Your Position]
HR Department
[Company Name]
[Contact Information]
'''

