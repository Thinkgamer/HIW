#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from hive.models import Session
import datetime
from django.http   import HttpResponseRedirect
# Create your views here.

@csrf_exempt
def phive(request,username):
    sess_list = Session.objects.all().order_by("-time")

    if request.method=="POST":
        sessionname = request.POST.get("sessionname")
        hql = request.POST.get("hql")
        # print(sessionname,hql)

        #如果是填写事务名的表单提交
        if sessionname:
            #将sessionname写入数据库
            sess=Session(uname=username,sessionname=sessionname,time=datetime.datetime.now())
            sess.save()
            return render_to_response("hive.html", {
                "name": username,
                "sessionname": sessionname,
                "sess_list":sess_list,
            })
        #如果是编写的sql提交
        if hql:
            from phive import run_hql
            sessionname=request.POST.get("session")
            #将提交的hql写入数据库
            sess= Session.objects.get(sessionname=sessionname)
            sess.context=hql
            sess.save()
            
            result = run_hql(hql)
            return render_to_response("hive.html", {
                "name": username,
                "sessionname":sessionname,
                "sess_list":sess_list,
                "result":result,
                "text_sql":hql,
            })

    else:
        return render_to_response("hive.html", {
            "name": username,
            "sess_list":sess_list,
        })


#if click old session
@csrf_exempt
def session(request,username,sessionname):
    sess_list = Session.objects.all().order_by("-time")
    if request.method=="POST":
       hql = request.POST.get("hql")
       #如果是编写的sql提交
       if hql:
           from phive import run_hql
           #sessionname=request.POST.get("session")
           #将提交的hql写入数据库
           sess= Session.objects.get(sessionname=sessionname)
           sess.context=hql
           sess.save()
           result = run_hql(hql)
           return render_to_response("hive.html", {
               "name": username,
               "sessionname":sessionname,
               "sess_list":sess_list,
               "result":result,
               "text_sql":hql,
           }) 
    else:
        hql = Session.objects.get(sessionname=sessionname).context
        return render_to_response("hive.html",{
           "name": username,
           "sessionname": sessionname,
           "sess_list":sess_list,
           "text_sql":hql,
        })   
