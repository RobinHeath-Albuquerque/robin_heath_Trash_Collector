from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50, default='name')
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default='address')
    zip_code = models.CharField(max_length=5, default='zipcode')
    service_day = models.CharField(max_length=50, default='service day')

    def __str__(self):
        return self.name
