import smtplib
from email.mime.text import MIMEText


def send_mail(customer,dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '5416e91cc38599'
    password = 'a975908e4128a5'
    message= f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>dealer: {dealer}</li><li>rating: {rating}</li><li>Comments: {comments}</li> "


    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Que Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email


    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())