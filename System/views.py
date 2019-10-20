from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from System.forms import UserForm, UserProfileForm, PatientForm
from System.main import get_patients, scheduler
from System.models import Patient, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import os
import json


def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)

    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect("/search")
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})


@login_required
@csrf_exempt
def perform_search(request):
    # params is just the string to compare the names with
    if request.is_ajax():
        if request.method == 'POST':
            return HttpResponse(get_patients(request.body))
    return HttpResponse(get_patients(""))


@login_required
def search(request):
    return render(request, 'search.html', {})


@login_required
def patient(request, patient_tel):
    tel = patient_tel
    patient = Patient.objects.get(telephone__contains=tel)
    # out = {}
    # out[patient.telephone] = {"name": patient.name, "meds": patient.medication, "notes": patient.notes}

    out = {"name": patient.name, "tel": patient.telephone, "notes": patient.notes, "meds": patient.medication}
    print(out)
    return render(request, 'patient.html', {"out": out})


@login_required
def add_patient(request):
    user = UserProfile.objects.filter(user__username=request.user)
    form = PatientForm
    return render(request, "add_patient.html", {"patient_form": form, "user": user})


@csrf_exempt
@login_required
def connect_patient(request, tel):
    print("CONNECT PATIENT RUN")
    user = UserProfile.objects.get(user__username=request.user);
    user.patients.append(tel)


@csrf_exempt
@login_required
def save_patient(request):
    if request.is_ajax():
        if request.method == 'POST':
            a = request.body
    data = a.decode("utf-8").split("_0_")
    print(data)
    da = []
    for i in data:
        da.append(i.split("__"))
    tel = da[0]
    print(tel[0])
    da = da[1:-1]
    patient = Patient.objects.get(telephone__contains=tel[0])
    patient.medication = []
    for i in da:
        patient.medication.append({"Medicine": i[0], "Time": i[1], "Message": i[2]})
    patient.save()
    # {"Medicine": "Panadol", "Time": "1700", "Message": "Take a Panadol (green bottle)"}
    response = {"name":"name"}
    return HttpResponse(json.dumps(response))

def schedule(request):
    scheduler()
    return "DONE BB's"