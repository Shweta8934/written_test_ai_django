from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    
    class Meta:
        app_label = 'writetset_frontend'