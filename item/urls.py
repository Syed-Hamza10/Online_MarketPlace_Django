from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'item'

urlpatterns = [
    path("<int:pk>/", detail, name = 'detail'),
    
]