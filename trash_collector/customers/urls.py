from django.urls import path, include
from . import views





# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('one_time_day/', views.one_time_day, name='one_time_day'),
    path('change/', views.change, name='change'),
    path('account_suspend/', views.account_suspend, name='account_suspend'),
    path('account/', views.account, name='account')



        ]

