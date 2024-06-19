from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False,blank=True,null=True)
    
    def __str__(self):
        return f"{self.title} added"
    
    # def get_absolute_url(self):
    #     return reverse('task-detail', kwargs={'pk':self.pk})
    
