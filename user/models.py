from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=127,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    update_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    post_permission = models.BooleanField(default=False)