# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import mongoengine
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
# user = authenticate(username=username, password=password)
# assert isinstance(user, mongoengine.django.auth.User)
connect('myday')
user=User.objects(username='qingyu')

def index(request):
    todos = user.day.todo
    return HttpResponse("Welcome!")
