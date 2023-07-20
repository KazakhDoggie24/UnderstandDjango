from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop_view(request):
    return render(request, 'main_shop.html')