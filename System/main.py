import pymongo
from System.models import Patient
import json
import schedule
import time
from sms import send_sms_reminder



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
    schedule.clear("medication_daily")
    for patient in Patient.objects.all():
        for med in patient.medication:
            schedule_sms(med["Time"][:2] + ":" + med["Time"][2:], patient.name, med["Medicine"], patient.telephone)

            # {"Medicine": "Panadol", "Time": "1700", "Message": "Take a Panadol (green bottle)"}]}


def schedule_sms(med_time, patient_name, patient_med, patient_tel):
    # time format hh:mm
    schedule.every().day.at(med_time).do(send_sms_reminder(patient_name, patient_med, patient_tel)).tag("medication_daily")
    while True:
        schedule.run_pending()
        time.sleep(1)


