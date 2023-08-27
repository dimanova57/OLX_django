from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
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


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15)
    balance = models.IntegerField(default=0)
    list_of_order = ArrayField(models.IntegerField(), default=list)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def by_product_and_add_order(self, product_id):
        self.list_of_order.append(product_id)
        product = Product.object.get(id=product_id)
        product.not_sold = False
        self.balance -= product.price
        super().save()

    def delete_order(self, product_id):
        self.list_of_order.remove(product_id)
        product = Product.object.filter(id=product_id)[0]
        author = Person.objects.filter(id=product.author)[0]
        author.balance += product.price
        super().save()


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # photo = None  # TODO create logic of loading photo!!! And ask on the lesson how better do it!!!
    title = models.CharField(max_length=100, default='Product')
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    published_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    not_sold = models.BooleanField(default=True)

    # def by_product_and_add_order(self, product_id):
    #     self.list_of_order.append(product_id)
    #     product = Product.object.get(id=product_id)
    #     product.not_sold = False
    #     self.balance -= product.price
    #     super().save()
    #
    # def delete_order(self, product_id):
    #     self.list_of_order.remove(product_id)
    #     product = Product.object.filter(id=product_id)[0]
    #     author = Person.objects.filter(id=product.author)[0]
    #     author.balance += product.price
    #     super().save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.published_date = timezone.now()
        super().save()

    def __str__(self):
        return self.title
