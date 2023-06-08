import smtplib
password = "ckuorxhtrofqrbkc"
sender = "Mr.Xayrullayev1506@gmail.com"
server = "smtp.gmail.com"
port = 465
reciever = "absaitovdev@gmail.com"
message = """
From: {}
To: {}
subject:
    github_link:
""".format(sender, reciever)

with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password)
    server.sendmail(sender, reciever, message)
    print("Sending email")