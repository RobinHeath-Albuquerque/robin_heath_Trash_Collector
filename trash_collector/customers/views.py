from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.urls import reverse


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # get the logged in user within any view function
    user = request.user
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }

    print(user)
    return render(request, 'customers/index.html', context)


def custinfo(request):
    context = {}
    return render(request, 'customers/custinfo.html', context)


def onetime(request):
    context = {}
    return render(request, 'customers/onetime.html', context)


def change(request):
    context = {}
    return render(request, 'customers/change.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        service_day = request.POST.get('service_day')
        new_customer = Customer(name=name, address=address, zip_code=zip_code, service_day=service_day, user=request.user)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')

def suspend(request):
    context = {}
    return render(request, 'customers/suspend.html', context)
