from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *
from main import forms
app_name = 'accounts'

urlpatterns = [
    path("signup/", signup, name = 'signup'),
    path("login/", auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form=LoginForm), name = 'login')
    
]