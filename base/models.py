from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=10000*10000, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image=models.ImageField( blank=True, default=None)
    
    class Meta():
        ordering=['-updated', '-created']
    
    def __str__(self):
        return self.title
    
class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,  on_delete=models.CASCADE)
    body=models.TextField()
    
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta():
        ordering=["-updated","-created"]
    
    def __str__(self):
        return self.body[:50]