"""
Definition of urls for MYCV.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin




urlpatterns = [
    path('',include('app.urls')),
   
    path('admin/', admin.site.urls),
]
