
# Create your views here.

from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.sites.models import Site

# ghfgdfgdfdf
# new_site = Site.objects.create(domain='foo1.com', name='foo1.com')
# print(new_site.id)
from employer.models import Employer
from .forms import EmployerForm, Login, Signup 
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def employer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
           form = EmployerForm(request.POST,request.FILES)
           if form.is_valid():
              form.save()
              messages.info(request, 'Your form has been submitted successfully !')
              form = EmployerForm()
        else:
          form = EmployerForm()
        return render(request, 'employer/employerform.html', {'form': form}) 
    else:
        form = EmployerForm()
    return render(request,'employer/employerform.html',{'form':form})


# Employer_signup
def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations !! You have signup successfully.')
            form.save()
            # user = form.save()
            # group = Group.objects.get(name='Signup')
            # user.groups.add(group)
            return HttpResponseRedirect('/signup/')
    else:
        form = Signup()
    return render(request, 'employer/signup.html', {'form': form})

# Log_in
def employer_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
          form = Login(request=request, data=request.POST)
          if form.is_valid():
            uname=form.cleaned_data['username']
            pwd=form.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Congratulations !! You have login successfully.')
                return HttpResponseRedirect('/employer/')
        else:
            form = Login()
        return render(request, 'employer/login.html',{'form':form}) 
    else:
        return HttpResponseRedirect('/employer/')          

def employer_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def search_employer(request):
    if request.method == "POST":
        query_name = request.POST.get('skills', None)
        if query_name:
            results = Employer.objects.filter(skills__contains=query_name)
            return render(request, 'employee/employersearch.html', {"results":results})
    return render(request, 'employee/employersearch.html')    