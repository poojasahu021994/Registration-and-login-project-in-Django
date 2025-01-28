from django.urls import path
from .import views

urlpatterns=[
    path ('', views.index,name='index'),
    path ('data/', views.data,name='data'),
    path ('register/', views.register,name='register'),
    path ('login/', views.login,name='login')
    ]