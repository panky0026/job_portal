from django.db import models

# Create your models here.
from multiprocessing import AuthenticationError
from django.db import models

# Create your models here.
class Employer(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField(max_length=300)
    company_name = models.CharField(max_length=100)
    #upload_company_logo= models.ImageField(upload_to ='uploads/',null=True)
    #company_GST_number= models.CharField(max_length=50,null=True)
    #pancard_number=models.CharField(max_length=10,null=True)
    experience= models.DecimalField(max_digits=10,decimal_places=2,null=True) 
    qualification=models.TextField(max_length=100,null=True)
    no_of_opening   = models.IntegerField()
    job_location = models.CharField(max_length=300)
    salary_range = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    skills = models.CharField(max_length=300)
    contact_person_name = models.CharField(max_length=100)
    contact_person_profile = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    choice_of_job= (
        ('1','work_from_home'),     
        ('2', 'work_from_office'),
        ('3','hybride'),
    )
    model_of_job = models.CharField(max_length=50,default="model_of_job",choices=choice_of_job)
    company_address = models.TextField(max_length=300,null=True)
    job_choice= (
        ('1','full_time'),     
        ('2', 'part_time'),
        ('3','intership'),
    )
    job_type = models.CharField(max_length=50,default="job_type",choices=job_choice)

class Signup(models.Model):
    user_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    models.EmailField( max_length=254) 

class Login(AuthenticationError):
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)