# myproject\blog\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')
]
