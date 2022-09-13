from django.db import models
import uuid

class Answer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    user= models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="answers")
    comment = models.ForeignKey("comments.Comment", on_delete=models.CASCADE, related_name="answers")