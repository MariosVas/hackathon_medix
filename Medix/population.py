import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DjangoSurvivalGame.settings')

import django
import datetime
django.setup
from System.models import Patient, UserProfile
from django.contrib.auth.models import User

patients = [
    {"name": "Marios",
     'notes': "He's like, an awful person, overdose him",
     'tel': "0035799728128",
     'meds': [{"Medicine":"Insulin", "Time":datetime.time(hour=17, minute=00), "Message":"Take your Insulin"},
            {"Medicine":"Placebo", "Time":datetime.time(hour=19, minute=00), "Message":"Take the red pill or the blue, same thing"}
              ]},
    {"name": "Ross",
     'notes': "Allergic to Penicilin",
     'tel': "00447522088933",
     'meds':[{"Medicine":"GUTSvitamin", "Time":datetime.time(hour=20, minute=00), "Message":"Take your Vitamins"},
             {"Medicine":"Panadol", "Time":datetime.time(hour=17, minute=00), "Message":"Take a Panadol (green bottle)"}]}
]




def add_patient(name, tel, notes, meds):
    Patient.objects.get_or_create(name=name, telephone=tel, notes=notes, medication=meds)

for p in patients:
    add_patient(p["name"], p['tel'], p['notes'], p['meds'])
