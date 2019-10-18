from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import os


def login(request):

    return render(request, 'login.html', {})


def search(request):

    return render(request, 'main.html', {})


@login_required
def patient(request):

    return render(request, 'patient.html', patient)