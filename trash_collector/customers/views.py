from django.apps import apps
from django.db.models.signals import post_save
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.template import context

from .models import Customer
from django.urls import reverse
import decimal


def index(request):
    # get the logged in user within any view function
    user = request.user
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }

    print(user)
    return render(request, 'customers/index.html', context)


def account(request):
    if request.method == 'GET':
        user = request.user
        Customer = apps.get_model('customers.Customer')
        customer = Customer.objects.get(user_id=user.id)
        context = {
            'customer': customer
        }

        return render(request, 'customers/account.html', context)
    else:
        return HttpResponseRedirect(reverse('customers:index'))


def one_time_day(request):
    if request.method == 'POST':
        user = request.user
        customer = Customer.objects.get(user_id=user.id)
        customer.one_time_day = request.POST.get('one_time_day')
        customer.save()

        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/one_time_day.html')


def account_suspend(request):
    if request.method == 'POST':
        user = request.user
        customer = Customer.objects.get(user_id=user.id)
        customer.suspend_start = request.POST.get('suspend_start')
        customer.suspend_end = request.POST.get('suspend_end')
        customer.account_active = False
        customer.save()

        return HttpResponseRedirect(reverse('customers:index'))
    else:

        return render(request, 'customers/account_suspend.html')


def change(request):
    if request.method == 'POST':
        user = request.user
        customer = Customer.objects.get(user_id=user.id)
        customer.service_day = request.POST.get('service_day')
        customer.save()

        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/change.html')


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        service_day = request.POST.get('service_day')
        new_customer = Customer(name=name, address=address, zip_code=zip_code, service_day=service_day)
        new_customer.user_id = user.id
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')
