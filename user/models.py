from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=127,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    password = models.CharField(max_length=20)
    update_at = models.DateTimeField()
    created_at = models.DateTimeField()
    post_permission = models.BooleanField(default=False)