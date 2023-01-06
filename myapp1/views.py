from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):

    isActive = True
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)


    date = datetime.datetime.now()
    name = "Tapbook"
    

    data = {
        "date": date,
        "isActive" :isActive,
        "name": name,
            }

    return render(request,"home.html",data)

def about(request):
    # return HttpResponse("<h1>About section</h1>")
    return render(request,"about.html",{})


def services(request):
    # return HttpResponse("<h1>Services available</h1>")
    return render(request,"services.html",{})