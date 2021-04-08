# Generated by Django 3.1.8 on 2021-04-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
