from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50, default=0)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    zip_code = models.IntegerField(default=0)
    email = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.name
