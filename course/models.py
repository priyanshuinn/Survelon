from django.db import models
from course.storage import OverwriteStorage
# Create your models here.

class post_data(models.Model):
    heading = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=100, blank=True)
    image = models.TextField(blank=True)
    post_body = models.TextField(blank=True)
    post_author = models.TextField(blank=True)

class upload_file(models.Model):
    video=models.FileField(upload_to='media',storage=OverwriteStorage())

    
