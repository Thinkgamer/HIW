#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
# Create your views here.

def index(request,name):
    return render_to_response("index.html",{
        "name":name,
    })