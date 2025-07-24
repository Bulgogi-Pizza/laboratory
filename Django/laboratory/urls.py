from django.contrib import admin
from django.urls import path
from myapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_world),
    path('calculate/<int:number>/', views.calculate_fib),
]