# from django.contrib.postgres.fields import ArrayField
# from django.db import models
# from django.contrib.auth.models import AbstractUser, PermissionsMixin
#
# # Create your models here.
# # from shop_main.models import Product

#
# class Person(AbstractUser, PermissionsMixin):
#     phone_number = models.CharField(max_length=15)
#     balance = models.IntegerField(default=0)
#     list_of_order = ArrayField(models.IntegerField(), default=list)

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
