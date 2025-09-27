# app/models.py
from django.db import models
# Default User model ko import karein
from django.contrib.auth import get_user_model

# Default User model ka reference
User = get_user_model()

class UserProfile(models.Model):
    # OneToOneField se UserProfile table ko default auth.User se jodenge
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Aapki extra fields
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    
    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Extra fields jo ab default User table se hat gaye hain, unko aap yahan add kar sakte hain:
    # is_admin = models.BooleanField(default=False) # Agar zaroori ho toh

    def __str__(self):
        return f"Profile for {self.user.email}"