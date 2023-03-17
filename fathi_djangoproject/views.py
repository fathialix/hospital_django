from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Patient


def index_page(request):
    data = Patient.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def edit_page(request):
    return render(request, "edit.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Patient(name=name, contact=contact, age=age, gender=gender)
        query.save()
        return redirect("index/")

        return render(request, 'index.html')


def deleteData(request, id):
    d = Patient.objects.get(id=id)
    d.delete()
    return redirect("index/")

    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        update_info = Patient.objects.get(id=id)
        update_info.name = name
        update_info.contact = contact
        update_info.age = age
        update_info.gender = gender

        update_info.save()

        return redirect("index/")

    d = Patient.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)


def index(request):
    return render(request, "index2.html")
