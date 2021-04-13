from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .models import Employees
from datetime import date
import datetime


# Create your views here.
# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    employees = apps.get_model('employees.Employees')
    return render(request, 'employees/index.html')


def localzip_employee(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_saturday = 'saturday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == employee.define_day:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
    return render(request, 'employees/index.html', context)


def one_time_pick_up(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    same_service_day = []
    for customer in customers:
        if customer.one_time_day == date.today() and customer.zip_code == employee.zip_code:
            same_service_day.append(customer)
            context = {
                'customers': same_service_day
            }
    return render(request, 'employees/index.html', context)


def define_day(request):
    if request.method == 'POST':
        user = request.user
        employee = Employees.objects.get(user_id=user.id)
        employee.define_day = request.POST.get('define_day')
        employee.save()
        return HttpResponseRedirect(reverse('employees:index'))

    return render(request, 'employees/index.html')


def active_accounts(request):
    context = {}
    return render(request, 'employees/active_accounts.html', context)


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employees(name=name, zip_code=zip_code)
        new_employee.user_id = user.id
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


def showdate(request):
    datetime.datetime.now()
    return render(request, 'employees/index.html')
