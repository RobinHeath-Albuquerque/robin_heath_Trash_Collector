from django.db import models



# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employees(models.Model):
    name = models.CharField(max_length=50, default=None)
    zip_code = models.CharField(max_length=6, default=None)
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE)
    define_day = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name
