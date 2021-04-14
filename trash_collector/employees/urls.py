from django.urls import path
from . import views
# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns
app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('define_day/', views.define_day, name='define_day'),
    path('localzip_employee/', views.localzip_employee, name='localzip_employee'),
    path('customer_in_zip', views.customer_in_zip, name='customer_in_zip'),
    path('one_time_pick_up/', views.one_time_pick_up, name='one_time_pick_up'),
    path('active_accounts/', views.active_accounts, name='active_accounts'),
    path('confirm_pickup/<int:customer_id>/', views.confirm_pickup, name='confirm_pickup'),
    path('create/', views.create, name='create')
]