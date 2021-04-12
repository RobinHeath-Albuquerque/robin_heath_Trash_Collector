from django.urls import path
from . import views
# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns
app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('localzip_employee_monday/', views.localzip_employee_monday, name='localzip_employee_monday'),
    path('localzip_employee_tuesday/', views.localzip_employee_tuesday, name='localzip_employee_tuesday'),
    path('localzip_employee_wednesday/', views.localzip_employee_wednesday, name='localzip_employee_wednesday'),
    path('localzip_employee_thursday/', views.localzip_employee_thursday, name='localzip_employee_thursday'),
    path('localzip_employee_friday/', views.localzip_employee_friday, name='localzip_employee_friday'),
    path('localzip_employee_saturday/', views.localzip_employee_saturday, name='localzip_employee_saturday'),
    path('localzip_employee_sunday/', views.localzip_employee_sunday, name='localzip_employee_sunday'),
    path('same_service_day_employee/', views.same_service_day_employee, name='same_service_day_employee'),
    path('one_time_pick_up_due_out/', views.one_time_pick_up_due_out, name='one_time_pick_up_due_out'),
    path('active_accounts/', views.active_accounts, name='active_accounts'),
    path('create/', views.create, name='create')
]