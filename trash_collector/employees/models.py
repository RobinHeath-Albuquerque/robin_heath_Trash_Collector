from django.db import models



# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employees(models.Model):
    name = models.CharField(max_length=50, default=0)
    zip_code = models.CharField(max_length=6)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
