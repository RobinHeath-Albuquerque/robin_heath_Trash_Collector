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
   if '<Customer.customers>'.objects.zip_code == Employees.zip_code:
       pass
       selected_customers = '<Customer.customers>'.objects
   else:
       #display nothing exists

    context = {
        'selected_customers': selected_customers
    }
    return render(request, 'employees/localzip_employee.html', context)


def one_time_pick_up_due_out(request):
    context = {}
    return render(request, 'employees/one_time_pick_up_due_out.html', context)


def active_accounts(request):
    context = {}
    return render(request, 'employees/active_accounts.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employees(name=name, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')
