from django.db import models


# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=10000)
    like = models.IntegerField(default=0)
