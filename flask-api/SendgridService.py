import sendgrid
from sendgrid.helpers.mail import *

'''Add your api_key for email support'''
sendgrid_api_key = ''


def send_email(email):
    sg = sendgrid.SendGridAPIClient(api_key='')
    from_email = Email("")
    to_email = To(email)
    subject = "Reset your password"
    reset = 'https://tye5zbnac5.execute-api.us-east-2.amazonaws.com/Prod/password'
    content = Content("text/plain",
                      'reset_password_url: https://tye5zbnac5.execute-api.us-east-2.amazonaws.com/Prod/password ')
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
