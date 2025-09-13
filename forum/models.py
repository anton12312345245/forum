from django.db import models
from django.contrib.auth.models import User



class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topic")

    def __str__(self):
        return self.title


class Post(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name="Post")
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} ({self.topic.title})"
    

