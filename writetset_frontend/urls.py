# writetset_frontend/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views # UI views के लिए

urlpatterns = [
    # 1. Login API Endpoint: JWT Tokens जनरेट करने के लिए
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # 2. Frontend UI View: Login Form दिखाने के लिए
    path('login/', views.login_page, name='login_page'),
]