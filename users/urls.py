from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.UserView.as_view()),
    path('users/login/', views.LoginView.as_view()),
]