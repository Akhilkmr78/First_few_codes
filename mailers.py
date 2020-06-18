import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Akhil Kumar'
email['to'] = '16m602@nith.ac.in'
email['subject'] = 'Sent from Pycharm!!'

email.set_content('Learning to grow')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('akhil.ed02@gmail.com', 'gerrard2')
    smtp.send_message(email)
    print('ok boss')
