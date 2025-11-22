from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('<int:pk>/', views.employee_details, name='employee_details')
]