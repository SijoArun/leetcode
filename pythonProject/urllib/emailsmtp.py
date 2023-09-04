import smtplib
from email.mime.text import MIMEText

body="Hi How are you"

msg=MIMEText(body)

msg["From"]="sijoarunachalam2@gmail.com"
msg["To"]="sijoarunachalam2@gmail.com"
msg["subject"]="Text Email"

server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()
server.login("mypythonapp","mwlxnpqmfvzrhxgh")
server.send_message(msg)
print("Mail sent")
server.quit()