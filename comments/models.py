import uuid

from django.db import models


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.CharField(max_length=130)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(

        "user.User", on_delete=models.CASCADE, related_name="comment_user"

    )
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="comment_post"
    )
