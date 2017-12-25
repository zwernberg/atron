from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()