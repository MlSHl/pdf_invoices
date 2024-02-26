import smtplib, ssl


def send_email(message):
    username = "mishi.beraia@gmail.com"
    password = "vbbd jtgd qzzp xplq"

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()
    receiver = "mishi.beraia@gmail.com"


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
