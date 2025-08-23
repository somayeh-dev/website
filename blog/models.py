from django.db import models

# Create your models here.
class Post(models.Model):
     title =models.CharField(max_length=100)
     content = models.TextField()
     content_views=models.IntegerField(default=0)
     status=models.BooleanField(default=False)
     publish_date = models.DateTimeField(null=True)
     created_date=models.DateTimeField(auto_now_add=True)
     update_date=models.DateTimeField(auto_now=True)