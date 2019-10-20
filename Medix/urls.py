"""Medix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from System import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.user_login, name='login'),
    url(r'^login/', views.user_login, name=''),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/', views.search, name='search'),
    url(r'^perform_search', views.perform_search, name='perform_search'),
    url(r'^patient/(?P<patient_tel>[\w\-]+)', views.patient, name="patient"),
    url(r'^add_patient', views.add_patient, name="add_patient"),
    url(r'^connect_patient', views.connect_patient, name="connect_patient"),
    url(r'^save_patient', views.save_patient, name="save_patient"),
    url(r'^schedule', views.schedule, name="schedule"),
    url(r'^patient_addition', views.patient_addition, name="patient_addition"),
]
