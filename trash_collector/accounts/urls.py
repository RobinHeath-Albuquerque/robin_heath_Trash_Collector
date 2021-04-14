from . import views

from django.urls import path


app_name = "accounts"
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]
