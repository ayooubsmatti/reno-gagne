from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('service/<str:pk>/', views.service, name="service"),

]
