#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
from django.http   import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def hdfsfile(request,username):
    from save.actionhdfs import get_all_file
    #如果是用户提交查询
    if request.method=="POST":
        path = request.POST.get("filepath")
        if path == "/":
            root_more=0
        else:
            root_more=1
        error=0
        try:
            mess_list = get_all_file(path)
        except:
            error="路径不存在或者为文件!"
            mess_list=[]
        return render_to_response("save.html", {
            "mess_list": mess_list,
            "path_value":path,
            "error":error,
            "root_more":root_more,
            "name":username,
        })
    #如果是url直接定位到该界面，默认返回/
    else:
        path="/"
        mess_list = get_all_file(path)
        return render_to_response("save.html",{
            "mess_list":mess_list,
            "path_value":path,
            "root_more":0,
            "name":username,
        })

#直接点击目录名进行下一级的查看
@csrf_exempt
def file(request,username,path):
    from save.actionhdfs import get_all_file
    path = path[5:]
    if path=="":
        root_more=0
    else:
        root_more=1
    try:
        error=0
        mess_list = get_all_file(path)
    except:
        mess_list=[]
        error="路径不存在或者为文件!"
    return render_to_response("save.html", {
        "mess_list": mess_list,
        "path_value": path,
        "root_more":root_more,
        "error":error,
        "name":username,
    })

#详情
@csrf_exempt
def more(request,username,path):
    from save.actionhdfs import show_more,get_all_file
    path=path.split("=")[1]
    try:
        error=0
        mess_list = get_all_file(path)
    except:
        error="路径不存在或者为文件!"
        mess_list=[]
    more_mess = show_more(path)
    return render_to_response("save.html",{
        "error":error,
        "more":1,
        "name":username,
        "mess_list": mess_list,
        "path_value": path,
        "more_mess":more_mess,
    })
#删除目录
def delete(request,username,path):
    new_path = "/".join(path.split("/")[:-1])
    from save.actionhdfs import delete_path
    delete_path(path[5:])
    return file(request,username,new_path)

@csrf_exempt
#创建目录
def mkdir(request,username,path):
    name = request.POST.get("mkdir") #用户提交的名字
    mk_path = path[5:] + "/" + name  #用来创建文件夹的名字
    from save.actionhdfs import mkdir_path
    mkdir_path(mk_path)       #创建文件夹
    return file(request,username,path)

@csrf_exempt
#重命名文件
def rename(request,username,path):
    name = request.POST.get("rename")  # 用户提交的名字
    rn_path = "/".join(path.split("/")[:-1])[5:] + "/" + name  # 用来重命名文件夹的名字
    from save.actionhdfs import rename_path
    rename_path(path[5:],rn_path)  # 重命名文件夹
    return HttpResponseRedirect("/save/file/%s/%s" % (username,"/".join(path.split("/")[:-1])) )

#下载文件
@csrf_exempt
def down(request,username,path):
    name = request.POST.get("download") #用户提交的下载路径
    file_path = path[5:]  #文件在hdfs上的目录
    from save.actionhdfs import down_file
    down_file(file_path,name)       #创建文件夹
    return file(request,username,"/".join(path.split("/")[:-1]) )

#上传文件
@csrf_exempt
def upload(request,username,path):
    name = request.POST.get("up")  # 用户提交的上传文件路径
    file_path = path[5:]  # 文件在hdfs上的目录
    from save.actionhdfs import upload_file
    upload_file(file_path,name)       #创建文件夹
    return file(request,username, path)


#待增加功能=====================================================
def read():
    print("如果不是目录显示该文件内容")