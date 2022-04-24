from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.CharField(max_length=400)
