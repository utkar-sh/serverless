import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_verification_email(send_from, send_to, subject, body):
    try:
        message = Mail(
            from_email = send_from,
            to_email = send_to,
            subject = subject,
            html_content = body
        )
        sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)

        print('Using Sendgrid API send ' + response + ' Status Code: ' + str(response.status_code) + ' ' + response.status_code + ' ' + response.body + ' ' + response.headers)

        return response
    
    except Exception as e:
        print(e)