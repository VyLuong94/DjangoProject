# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from mysite.views import detect_anomalies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', detect_anomalies, name='detect'),
    path('detect-anomalies/',detect_anomalies, name='detect_anomalies'), 
    # path('detect/', detect_anomalies, name='detect'),
    # Add other URL patterns as needed
]




