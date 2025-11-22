from django.http import HttpResponse
from django.shortcuts import render
from Employee.models import Employees
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'index.html')


def home(request):
    employees = Employees.objects.all()
    context = {
        'emp': employees,
    }
    return render(request, 'home.html', context)


def employee_details(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    context = {
        'emp': employee
    }
    return render(request, 'employee_detail.html', context)
