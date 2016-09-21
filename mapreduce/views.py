from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def mr(request,username):
    if request.method == "POST":
        jar_path = request.POST.get("jar_path")
        input_path = request.POST.get("inputfile_path")
        output_path =request.POST.get("outputfile_path")
        main_class = request.POST.get("main_class_name")
        from mapreduce.runjisuan import runmr
        runmr(jar_path,input_path,output_path,main_class)

        return render_to_response("mapreduce.html", {
            "name": username,
            "jar_path":jar_path,
            "input_path":input_path,
            "output_path":output_path,
            "main_class_name":main_class,
        })
    else:
        return render_to_response("mapreduce.html",{
            "name":username,
        })