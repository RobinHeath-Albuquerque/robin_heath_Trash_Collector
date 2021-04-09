from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50, default='name')
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default=0)
    zip_code = models.CharField(max_length=5, default=0)
    service_day = models.CharField(max_length=50, default=0)
    address = models.CharField(max_length=50, default='address')
    zip_code = models.CharField(max_length=5, default='zip_code')
    service_day = models.CharField(max_length=50, default='service_day')

    def __init__(self):
        return self.name



