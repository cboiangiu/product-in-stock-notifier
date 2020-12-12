import smtplib, ssl
from email.message import EmailMessage

class Emailer:
    def __init__(self, host, port, email, password):
        self.host = host
        self.port = port
        self.email = email
        self.password = password
        self.create_server()

    def __del__(self):
        self.server.quit()

    def create_server(self):
        self.server = smtplib.SMTP_SSL(self.host, self.port, context=ssl.create_default_context(), timeout=5)
        self.server.login(self.email, self.password)

    def send_email(self, recipient, subject, body):
        try:
            self.server.noop()[0]
        except:
            self.server.quit()
            self.create_server()
        message = EmailMessage()
        message["Subject"] = subject
        message["From"] = self.email
        message["To"] = recipient
        message.set_content(body)

        self.server.sendmail(self.email, recipient, message.as_string())
