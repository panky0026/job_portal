from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile', 'adhar_number', 'email', 'qualification', 'skills', 'job_title', 'job_type', 'job_location', 'mode_of_job', 'experiences', 'resume', 'profile_pic', 'expected_salary', 'street', 'city', 'state', 'zip', 'country']
