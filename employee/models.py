from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    fullname = models.CharField(max_length=256)
    is_admin = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_media', null=True, blank=True)