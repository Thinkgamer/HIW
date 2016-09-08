from django.shortcuts import render_to_response

# Create your views here.
def mr(request,username):

    return render_to_response("jisuan.html",{
        "name":username,
    })