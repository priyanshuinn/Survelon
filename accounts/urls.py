from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name = 'accounts-register'),
    path('login', views.login, name = 'accounts-login'),
    path('logout', views.logout, name = 'accounts-logout'),
    path('massage', views.massage, name = 'accounts-massage'),
    path('checkotp', views.check_otp, name = 'accounts-checkotp'),

]