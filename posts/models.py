from tokenize import group
from django.db import models
import uuid

class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.TextField(null=False, blank=False)
    media = models.TextField()
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="posts")
    group_id = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name="posts")