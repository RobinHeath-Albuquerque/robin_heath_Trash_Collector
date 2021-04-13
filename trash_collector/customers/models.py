
from django.db import models

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50, default=None)
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default=None)
    zip_code = models.CharField(max_length=5, default=None)
    service_day = models.CharField(max_length=50, default=None)
    one_time_day = models.DateField(null=True, blank=True)
    account_balance = models.IntegerField(default=0)
    suspend_start = models.DateField(null=True, blank=True)
    suspend_end = models.DateField(null=True, blank=True)
    account_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


