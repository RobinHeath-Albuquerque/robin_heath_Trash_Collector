from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50, default=None)
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default=None)
    zip_code = models.CharField(max_length=5, default=None)
    service_day = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name



