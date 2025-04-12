from django.db.models import CASCADE
from django.db import models
from user.models import User
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)

    class Meta:
        ordering = ["-created"]