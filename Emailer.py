import smtplib, ssl
from credentials import credentials
from email.mime.text import MIMEText

class email():
    def __init__(self):
        self.username,self.password = credentials()


def send_mail(info1,info2):
    user,password = credentials()
    receivers = ["sirkingkeano@gmail.com"]
    body_of_email = f"A new venue with available slots {info1} was added to list and has {info2}place(s) available for vaccination"

    msg = MIMEText(body_of_email, "html")
    msg["Subject"] = "Ny vaccinationstid adderad"
    msg["From"] = "Vaccinationshjälpen"

    s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
    s.login(user = user, password = password)
    s.sendmail(user, receivers, msg.as_string())
    s.quit()
