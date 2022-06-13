from re import sub
import smtplib
import ssl
from email.message import EmailMessage

from django.dispatch import receiver

subject = "Email from Python"
body = "This is a test email from python"
sender_email = "mr.tringuyen1225@gmail.com"
receiver_email = "mr.tringuyen1225@gmail.com"
password = input("Enter a password: ")


message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

# sending as HTML
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")
# give is security context so we can use smtplib
# to connect to Gmal server
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Successfully send an email")
