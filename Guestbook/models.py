from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"