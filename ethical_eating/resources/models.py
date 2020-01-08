from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import statistics as stat


# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=10000)
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    site = models.URLField()
    cover = models.ImageField(upload_to='cover/')

    def __str__(self):
        return f'{self.title}'


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    site = models.URLField()
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_avg(self):
        if self.reviews.all():
            return stat.mean([review.rate for review in self.reviews.all()])
        else:
            None


class Review(models.Model):
    rate = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                      MinValueValidator(1)])
    author = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=500, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews', null=True)

    def __str__(self):
        return f'{self.text}'



