from django.db import models

# Create your models here.


class Stock(models.Model):
    stock_name = models.CharField(max_length=100, unique=True)
    video_link = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    active_flag = models.BooleanField(default=True)
