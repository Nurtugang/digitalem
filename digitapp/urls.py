from django.urls import path 
from digitapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('how', how, name='how'),
    path('how/<slug:lab_slug>/', lab, name='lab'),
    path('how/<slug:lab_slug>/<slug:field_slug>/projects/', projects, name='projects'),
    path('how/<slug:lab_slug>/projects/', all_projects, name='all_projects'),
    path('how/<slug:lab_slug>/<slug:field_slug>/<slug:project_slug>/', project, name='project'),

    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),

    path('contact_form', contact_form, name='contact_form'),
    path('mailing_form', mailing_form, name='mailing_form'),


]