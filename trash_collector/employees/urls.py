from django.urls import path
from . import views
# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns
app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('localzip_employee/', views.localzip_employee, name='localzip_employee'),
    path('one_time_pick_up_due_out/', views.one_time_pick_up_due_out, name='one_time_pick_up_due_out'),
    path('active_accounts/', views.active_accounts, name='active_accounts'),
    path('create/', views.create, name='create')
]