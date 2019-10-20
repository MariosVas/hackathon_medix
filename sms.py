import os
from twilio.rest import Client
import arrow
import schedule
from System.models import Patient
# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# create client object
client = Client(account_sid, auth_token)


def send_sms_reminder(name, medication, tel):
    """Send a reminder to a phone using Twilio SMS"""
    med_time = arrow.get(medication['Time'])
    body = 'Hi {0}. {1} at {2}.'.format(
            name,
            medication['Message'],
            med_time.format('h:mm a')
        )

    client.messages.create(
            body=body,
            to=tel,
            from_='+441625800133',
        )
