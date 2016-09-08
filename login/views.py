#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from save.actionhdfs import login_mkdir
# Create your views here.

@csrf_exempt
def login(request):
    if request.method=="POST":
        name = request.POST.get("name")
        passwd = request.POST.get("passwd")
        if name=="gyt" and passwd == "gyt":
            #给当前用户在hdfs下创建一个文件夹
            login_mkdir(name)
            return HttpResponseRedirect("/index/index/%s" % name)
    else:
        return render_to_response("login.html",{

        })