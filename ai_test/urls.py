# ai_test/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints और UI दोनों के लिए writetset_frontend app को include करें
    path('', include('writetset_frontend.urls')),
]