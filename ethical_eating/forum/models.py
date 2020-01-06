from django.db import models


# Create your models here.

class Thread(models.Model):
    text = models.CharField(max_length=150)
    creator = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.text}'


class Comment(models.Model):
    text = models.CharField(max_length=250)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    creator = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.text}'
