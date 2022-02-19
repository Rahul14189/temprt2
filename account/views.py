from django.shortcuts import render
from account.models import Employee, Temp, Dev
from .import models
from django.contrib import messages
from django import forms


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('person')
        # name = form.cleaned_data('person')
        # data = Employee.objects.get(person=name)
        data_1 = Employee.objects.filter(person= name)
        # data_2 = Employee.objects.get(person=name)
        # data_3 = Employee.objects.get(person=name)
        danger = Employee.objects.filter(temp='100')
        context = {'data_1':data_1, 'danger':danger}
        return render(request, 'account/index.html', context)

    return render(request, 'account/index.html', context=None)

def home(request):

    if request.method == 'POST':
        person = request.POST.get('person')
        date = request.POST.get('date')
        temp = request.POST.get('temp')
        device = request.POST.get('device')
        employee = Employee.objects.create(person=person, date=date, temp=temp, dev=device)
        # Employee.objects.create(person=person, date=date, temp=temp, dev=device)
        # Employee.objects.create(person=person, date=date, temp=temp)
        messages.success(request, 'Data Stored Successfully')
        return render(request, 'account/home.html', context=None)
    else:
        messages.error(request, 'Please Enter Valid Data')
        return render(request, 'account/home.html', context=None)

    return render(request, 'account/home.html', context=None)


