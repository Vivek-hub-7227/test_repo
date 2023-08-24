import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.office365.com"
sender_email = "noreply@fi911.com"
receiver_email = "Vivek.m@911fintech.com"
password = "Lop72698"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  
    server.starttls(context=context)
    server.ehlo()  
    server.login(sender_email, password)
    print("logged in")
    server.sendmail(sender_email, receiver_email, message)
    print("email sent")