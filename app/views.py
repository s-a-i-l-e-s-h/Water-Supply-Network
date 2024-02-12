from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import sample,tryit,doit


def index(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())
def waterreq(request):
    mydata = sample.objects.all()
    if (mydata != ""):
        return render(request, "waterreq.html", {"sample": mydata})
    else:
        return render(request,"waterreq.html")
def addData(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone_no = request.POST["phone_no"]
        alternative_phoneno = request.POST["alternative_phoneno"]
        address= request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        litre = request.POST["litre"]

        obj = sample()
        obj.name = name
        obj.phone_no = phone_no
        obj.alternative_phoneno = alternative_phoneno
        obj.address = address
        obj.city = city
        obj.state = state
        obj.litre = litre
        obj.save()
        mydata = sample.objects.all()
        return redirect("waterreq")
    return render(request,"waterreq.html")

def complaint(request):
    mydata = tryit.objects.all()
    if (mydata != ""):
        return render(request, "complaint.html", {"tryit": mydata})
    else:
        return render(request, "complaint.html")


def dataa(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone_no = request.POST["phone_no"]
        aadhar = request.POST["aadhar"]
        address = request.POST["address"]


        obj = tryit()
        obj.name = name
        obj.phone_no = phone_no
        obj.aadhar = aadhar
        obj.address = address
        obj.save()
        mydata = tryit.objects.all()
        return redirect("complaint")
    return render(request, "complaint.html")


def contact(request):
    mydata = doit.objects.all()
    if (mydata != ""):
        return render(request, "contact.html", {"doit": mydata})
    else:
        return render(request, "contact.html")

def datum(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]


        obj = doit()
        obj.name = name
        obj.email = email
        obj.message = message
        obj.save()
        mydata = doit.objects.all()
        return redirect("contact")
    return render(request, "contact.html")
def report(request):
    template=loader.get_template("report.html")
    return HttpResponse(template.render())
