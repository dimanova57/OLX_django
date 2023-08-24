from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView

from .forms import ProductForm
from .models import Product, Condition, Category, Place
from .servise import product_by_query

def create_products():
    # Отримати користувача для прив'язки до автора продукту
    user = Product.objects.first().author  # Зараз я використовую першого користувача, змініть це на свій спосіб отримання користувача

    # Створити 30 продуктів
    for i in range(30):
        product = Product(
            author=user,
            title=f'Product {i + 1}',
            condition=Condition.objects.first(),  # Зараз я використовую перший стан, змініть це на свій спосіб отримання стану
            category=Category.objects.first(),  # Зараз я використовую першу категорію, змініть це на свій спосіб отримання категорії
            place=Place.objects.first(),  # Зараз я використовую перше місце, змініть це на свій спосіб отримання місця
            description=f'This is product {i + 1}',
            price=(i + 1) * 10,  # Приклад ціни
        )
        product.save()



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



# 1. Додати додавання продуктів - і бекенд і фронтенд !!!!Done!!!!
# 2. Головна сторінка (рубрики та перегляд 10 оголошень)
# 3. Пошук по назві та опису та місцю
# 4. Перегляд сторінки продукту та можливість оцінка
# 5. Додати authorization !!!! DONE !!!!
# 6. Сторінка Наталії
# 7. Купівля
