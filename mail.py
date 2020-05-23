import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "deeptimlop@gmail.com"
receiver_email = "tiwari.deepti262@gmail.com"
password = "mlop@2020"
message = """\
Subject: JOB SUCCESSFUL

Dear Admin, 

All the jobs in MLOP TASK3 jon chain is succesfully executed and the model is trained with equal or more than 80% accuracy.
Have a nice day!!!!

"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
