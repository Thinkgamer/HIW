from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from save.actionhdfs import *
# Create your views here.
@csrf_exempt
def hdfsfile(request):

    if request.method=="POST":
        pass
    else:
        path="/"
        mess_list = get_all_file(path)
        return render_to_response("save.html",{
            "mess_list":mess_list,
        })