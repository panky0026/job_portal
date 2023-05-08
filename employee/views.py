from django.shortcuts import render,redirect, HttpResponseRedirect,HttpResponse
from .forms import EmployeeForm
from django.contrib import messages
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .models import Employee
# Create your views here.

def employee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your form has been submitted successfully !')
                form = EmployeeForm()
        else:
            form = EmployeeForm()
        return render(request, 'employee/employeeform.html', {'form': form}) 
    else:
        return HttpResponseRedirect('/employee/emp_login/')               

def employee_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            group = Group.objects.get(name='Employee')
            user.groups.add(group)
            messages.info(request, 'Your form has been submitted...!')
            return HttpResponseRedirect('/employee/emp_login/')
    else:
        form = SignupForm()
    return render(request, 'employee/signup.html', {'form': form})   

def login_required(function):
    def employee_login(request, *args, **kwargs):
        if 'name' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('/employee/emp_login/')
    return employee_login


def employee_login(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print(user_name)
        try:
            user = Employee.objects.get(email=user_name)
            print(user)
            if user.password == password:
                print("ok........")
                request.session['name'] = user.email
                # messages.success(request, ' loging Success.')
                print("ok........")
                return redirect('/employee/dashboard', {'u_name': user})
            else:
                print('invalid password !')
                # messages.success(request, 'invalid password !')
        except:
            print('user does not exist !')
            # messages.success(request, 'user does not exist !')
    form = LoginForm()        
    return render(request, 'employee/login.html',{'form': form})

@login_required
def empDashboard(request):
    return render(request, 'employee/home.html')

    # return HttpResponse('dashboard')

# def employee_login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = LoginForm(request=request, data=request.POST)
#             print(request.POST)

#             if form.is_valid():
#                 print('ok...........')
#                 uname = form.cleaned_data['username']
#                 pwd = form.cleaned_data['password']
#                 print(uname)
#                 print(pwd)
#                 user = authenticate(username=uname, password=pwd)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, 'logged in successfully...!')
#                     return HttpResponseRedirect('/employee/emp/')
#             else:
#                 print(form.errors.as_data())
#                 print('no...........')        
#         else:
#             form = LoginForm()
#         return render(request, 'employee/login.html', {'form': form})       
#     else:
#         return HttpResponseRedirect('/employee/emp/')             

def employee_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def search_employee(request):
    if request.method == "POST":
        query_name = request.POST.get('skills', None)
        if query_name:
            results = Employee.objects.filter(skills__contains=query_name)
            return render(request, 'employee/employeesearch.html', {"results":results})
    return render(request, 'employee/employeesearch.html') 
