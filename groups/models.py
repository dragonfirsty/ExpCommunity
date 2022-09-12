from django.db import models
import uuid

class Group(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20,unique=True)
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="group_user")