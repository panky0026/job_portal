from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    adhar_number = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length = 300)
    qualification = models.CharField(max_length=100, null=True)
    skills = models.CharField(max_length=300)
    job_title = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=100, null=True)
    job_location = models.CharField(max_length=100, null=True)
    mode_of_job = models.CharField(max_length=100, null=True)
    experiences = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume')
    profile_pic = models.ImageField(upload_to='profile')
    expected_salary = models.DecimalField(max_digits=20, decimal_places=2)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=50)
    country = models.CharField(max_length=100)