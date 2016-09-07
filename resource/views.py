#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
from resource.models import node
# Create your views here.

def resource(request,name):
    return render_to_response("resource.html",{
        "allmess_flag":1,
        "name":name,
    })

#各个节点的信息
def nodemess(request,name):
    node_list = node.objects.all()
    return render_to_response("resource.html", {
        "node_flag":1,
        "name": name,
        "node_list":node_list,
    })