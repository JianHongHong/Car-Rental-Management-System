from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import CsrfViewMiddleware
from django.views.decorators.csrf import csrf_exempt, csrf_protect#to use csrf exempt
from django.contrib.auth.hashers import make_password
from crcapp.models import Store, Employee, Customer, Vehicle, Order, OrderFor#If the model is used in the view file
from django.utils import timezone
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.sessions.models import Session
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from crcapp.controllers import authentication, staff, vehicle,orders, customer

# Developer: Aidan
def notLoggedIn(request):
    messages = "Access Denied!"
    request.session['msg'] = messages
    request.session['mtype'] = 'd'
    return redirect('/login')

# Developer: Aidan
def accessDeniedHome(request):
    messages = "Access Denied!"
    request.session['msg'] = messages
    request.session['mtp'] = 'd'
    return redirect('/management/home')
    
# Developer: Aidan
# Logoff action
def logoff(request, messages=""):
    messages = "Successfully logged off."
    authentication.Authentication.logout(request)
    request.session['msg'] = messages
    request.session['mtype'] = 'i'
    return redirect('/login')