
from django.contrib import admin
from django.urls import path, include

import chartapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chartapp.urls')),
]
