#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def login(request):
    if request.method=="POST":
        name = request.POST.get("name")
        passwd = request.POST.get("passwd")
        if name=="gyt" and passwd == "gyt":
            return HttpResponseRedirect("/index/index/%s" % name)
    else:

        return render_to_response("login.html",{

        })