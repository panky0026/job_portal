from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('emp/', views.employee, name='employee'),
    path('emp_signup/', views.employee_signup, name='emp_signup'),
    path('emp_login/', views.employee_login, name='emp_login'),
    path('emp_logout/', views.employee_logout, name='emp_logout'),
    path('s_employee/', views.search_employee, name='s_emp'),
    # nk
    path('dashboard/', views.empDashboard, name='s_emp'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
