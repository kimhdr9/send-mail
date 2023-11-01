import getpass
import smtplib
import os

HOST=os.getenv('SMTP_HOST')
PORT=os.getenv('SMTP_PORT')
FROM=os.getenv('SMTP_FROM')
TO=os.getenv('SMTP_TO')
print(f"host : {HOST}")
PASSWORD=getpass.getpass("Entrez le mot de passe :")

MESSAGE = """ Subject : Mail sent using python
Hi gmail,

This email is a test

Cheers

"""

smtp=smtplib.SMTP(HOST,PORT)

status_code, reponse = smtp.ehlo()

print(f" Retour serveur : {status_code} {reponse}")

status_code, reponse = smtp.starttls()

print(f" Starting TLS connection : {status_code} {reponse}")

status_code, reponse = smtp.login(FROM,PASSWORD)

print(f" Logging in : {status_code} {reponse}")

try :
    smtp.sendmail(FROM,TO,MESSAGE)
except ValueError :
    status_code,reponse = smtplib.SMTPDataError()
    print(f"code {status_code} message : {reponse}")
finally :
    # quitte smtp
    smtp.quit()

