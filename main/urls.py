from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name='shop_view'),  # Пустой путь для главной страницы
]