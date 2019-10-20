import os
from twilio.rest import Client

# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# create client object
client = Client(account_sid, auth_token)


def send_sms_reminder(patient_name, patient_message, patient_tel):
    """Send a reminder to a phone using Twilio SMS"""

    body = 'Hi {0}. {1}.'.format(
            patient_name,
            patient_message,
        )

    client.messages.create(
            body=body,
            to=patient_tel,
            from_='+441625800133',
        )
