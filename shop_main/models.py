from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # photo = None  # TODO create logic of loading photo!!! And ask on the lesson how better do it!!!
    title = models.CharField(max_length=100, default='Product')
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    description = models.TextField()
    price = models.IntegerField()
    not_sold = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.published_date = timezone.now()
        super().save()

    def __str__(self):
        return self.title
