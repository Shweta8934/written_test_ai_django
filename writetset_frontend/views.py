# writetset_frontend/views.py
from django.shortcuts import render
# TokenObtainPairView JWT के लिए views.py में import करने की ज़रूरत नहीं है

# UI View: यह सिर्फ़ login.html template को रेंडर करेगा
def login_page(request):
    return render(request, 'writetset_frontend/login.html')