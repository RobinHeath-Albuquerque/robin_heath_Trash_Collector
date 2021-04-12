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


def localzip_employee_monday(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_monday = 'monday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == service_day_monday:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
        else:
            context = {}
    return render(request, 'employees/index.html', context)


def localzip_employee_tuesday(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_tuesday = 'tuesday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == service_day_tuesday:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
        else:
            context = {}
    return render(request, 'employees/index.html', context)


def localzip_employee_wednesday(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_wednesday = 'wednesday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == service_day_wednesday:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
        else:
            context = {}
    return render(request, 'employees/index.html', context)


def localzip_employee_thursday(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_thursday = 'thursday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == service_day_thursday:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
        else:
            context = {}
    return render(request, 'employees/index.html', context)


def localzip_employee_friday(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_friday = 'friday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == service_day_friday:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
        else:
            context = {}
    return render(request, 'employees/index.html', context)


def localzip_employee_saturday(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_saturday = 'saturday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == service_day_saturday:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
        else:
            context = {}
    return render(request, 'employees/index.html', context)


def localzip_employee_sunday(request):
    user = request.user
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    service_day_sunday = 'sunday'
    same_zipcode = []
    for customer in customers:
        if customer.zip_code == employee.zip_code and customer.service_day == service_day_sunday:
            same_zipcode.append(customer)
            context = {
                'customers': same_zipcode
            }
        else:
            context = {}
    return render(request, 'employees/index.html', context)


def same_service_day_employee(request):
    user = request.user
    day_of_the_week = 'saturday'
    employee = Employees.objects.get(user_id=user.id)
    Customer: object = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    same_service_day = []
    for customer in customers:
        if customer.service_day == day_of_the_week:
            same_service_day.append(customer)
            context = {
                'customers': same_service_day
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
