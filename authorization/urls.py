from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SignupView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
