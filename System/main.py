import pymongo
from System.models import Patient
import json
import schedule
import time
import os
from twilio.rest import Client
from sms import send_sms_reminder


# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# create client object
client = Client(account_sid, auth_token)


def get_patients(params):
    to_search = params.decode("utf-8").split("=")[1]
    to_search = "".join(to_search)
    if to_search == "":
        data = Patient.objects.all()
    else:
        data = Patient.objects.filter(name__contains=to_search)
    output = {}
    for patient in data:
        output[patient.telephone] = {"name": patient.name, "notes": patient.notes}

    return json.dumps(output)


def scheduler():
    #schedule.clear("medication_daily")
    for patient in Patient.objects.all():
        for med in patient.medication:
            schedule.every().day.at(med["Time"][:2] + ":" + med["Time"][2:]).do(send_sms_reminder,
                                                 patient_name=patient.name, patient_message=med['Message'],
                                                 patient_tel=patient.telephone).tag("medication_daily")
            print("Job scheduled at {}.".format(med["Time"][:2] + ":" + med["Time"][2:]))
    while True:
        schedule.run_pending()
        time.sleep(60)
