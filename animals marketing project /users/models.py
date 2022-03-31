
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=50, null=False,blank=False)
    last_name=models.CharField(max_length=50,null=False,blank=False)
    email=models.EmailField(max_length=100,null=False,blank=False)
  