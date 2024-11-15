from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from datetime import timedelta

def insert_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            
            # Calculate leap years and non-leap years in the date range
            leap_years = 0
            non_leap_years = 0
            current_year = employee.start_date.year
            end_year = employee.end_date.year
            
            for year in range(current_year, end_year + 1):
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    leap_years += 1
                else:
                    non_leap_years += 1

            # Set calculated counts
            employee.leapyear_count = leap_years
            employee.non_leapyear_count = non_leap_years
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'insert_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})