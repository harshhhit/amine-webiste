from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    emai_token = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
        return self.user.username
    

##This model:
    # Extends Django’s built-in User model without modifying it
    # Adds fields like phone number, address, and email verification
    # Makes profiles easily accessible via user.profile
    # Adds a clean string representation via __str__ Create your models here.
