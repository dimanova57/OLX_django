from django.urls import path
from .views import MainPageView, AddProductView, CategoriesView, CategoriePageView, ProductPageView, UserPageView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('add_product', AddProductView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('categories/<int:id>', CategoriePageView.as_view()),
    path('product/<int:id>', ProductPageView.as_view()),
    path('profile', UserPageView.as_view()),
]
