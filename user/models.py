import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    post_permission = models.BooleanField(default=False, blank=True)
    groups = models.ManyToManyField("groups.Group", related_name="user_groups")
    
    REQUIRED_FIELDS = [
        "email",
        "first_name",
        "last_name",
        "birthdate",
        "post_permission",
    ]

