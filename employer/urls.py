from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('employer/', views.employer, name='employer'),
    path('signup/', views.signup, name='signup'),
    path('emp_login/', views.employer_login, name='emp_login'),
    path('emp_logout/', views.employer_logout, name='emp_logout'),
    path('s_employer/', views.search_employer, name='s_emp'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

