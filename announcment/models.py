from django.db import models
from django.contrib.auth.models import User

class Announcment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



#<a href="{% url 'announcment:announcment-create' %}">створити Оголошеня</a>