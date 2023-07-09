import sendgrid_function
import json

SENDER = "utkarsh@stage.utkarshneu.me"

def lambda_handler(event_message, context):

    print("SNS event message: " + event_message)

    event = json.loads(event_message['Records'][0]['Sns']['Message'])

    recipient_email = event['recipient_email']
    recipient_name = event['recipient_name']
    verification_link = event['verification_link']
    
    subject = '[csye6225-webapp-account-verification] Verify your account'
    body = 'Hi ' + recipient_name + ',\n' + 'Please click the following link to verify your account.\n' + verification_link + ' Thank you!'
        
    response = sendgrid_function.send_verification_email(SENDER, recipient_email, subject, body)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
