from django.urls import path
from .views import MainPageView, AddProductView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('add_product', AddProductView.as_view()),
]
