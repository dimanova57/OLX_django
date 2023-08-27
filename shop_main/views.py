from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView

from .forms import ProductForm
from .models import Product, Condition, Category, Place
from .servise import product_by_query


class MainPageView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = product_by_query(self.request)
        context['products'] = products
        return context


class AddProductView(CreateView):
    template_name = 'add_product.html'
    model = Product
    form_class = ProductForm  # TODO create product form
    success_url = '/'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)


class CategoriesView(TemplateView):
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoriePageView(TemplateView):
    template_name = 'categorie_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.kwargs['id'], not_sold=True)
        return context


class ProductPageView(TemplateView):
    template_name = 'product_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['product'] = Product.objects.filter(id=self.kwargs['id'])[0]
        except:
            pass
        return context


class UserPageView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_of_products = list()
        print(self.request.user.id)
        person = User.objects.get(id=self.request.user.id)
        if person.userprofile.list_of_order:
            for product_id in person.userprofile.list_of_order:
                list_of_products.append(Product.objects.get(id=product_id))
            context['products'] = list_of_products
        context['user'] = self.request.user
        return context


class BalanceView(CreateView):
    template_name = 'add_product.html'
    model = Product
    form_class = ProductForm  # TODO create product form
    success_url = '/'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)



# 1. Додати додавання продуктів - і бекенд і фронтенд !!!!Done!!!!
# 2. Головна сторінка (рубрики та перегляд 10 оголошень) !!!Done!!!
# 3. Пошук по назві та опису та місцю!!!DONE!!!
# 4. Перегляд сторінки продукту та можливість оцінка
# 5. Додати authorization !!!! DONE !!!!
# 6. Сторінка Наталії
# 7. Купівля
