from django.contrib import admin

from employer.models import Employer

# Register your models here.
@admin.register(Employer)
class EmployerformAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'job_description', 'company_name', 'no_of_opening', 'job_location', 'salary_range', 'skills', 'contact_person_name', 'contact_person_profile', 'mobile', 'email', 'company_address','model_of_job','experience','qualification']
