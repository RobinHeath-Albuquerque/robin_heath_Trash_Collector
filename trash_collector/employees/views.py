from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse

from .models import Employees


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    employees = apps.get_model('employees.Employees')

    return render(request, 'employees/index.html')


def localzip_employee(request):
    user = request.user
    employee = Employees.object.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
    return render(request, 'employees/index.html', context)


def one_time_pick_up_due_out(request):
    context = {}
    return render(request, 'employees/one_time_pick_up_due_out.html', context)


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
