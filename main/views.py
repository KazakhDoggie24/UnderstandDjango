from django.shortcuts import render
from django.http import HttpResponse
from .models import Address, People, Category, Store, Product
import os
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.storage import FileSystemStorage

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View

from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from rest_framework import generics
from .serializers import ASerializer, PeopleSerializer, CSerializer, SSerializer, PSerializer

from .forms import LoginUserForm, RegisterUserForm, AddressForm, CreditCardForm

# Create your views here.

def shop_view(request):
    return render(request, 'main_shop.html')

def products_view(request):
    return render(request, 'products.html')

# def login_view(request):
    # if request.method == 'POST':
    #    username = request.POST['username']
    #    password = request.POST['password']
    #    user = authenticate(request, username = username, password = password)
    #    if user is not None:
        #   login(request, user)
        #   return redirect('home')
    #    else:
        # return render(request, 'login.html', {'error_message': 'Неправильное имя пользователя или пароль.'})
    # return render(request, 'login.html')
# 
# def login_view(request):
    # if request.method == 'POST':
        # form = LoginUserForm(request.POST)
        # if form.is_valid():
            # pass
    # else:
        # form = LoginUserForm()
    # return render(request, 'login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop_view')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Неправильное имя пользователя или пароль.'})
    else:
        form = LoginUserForm()
    
    return render(request, 'login.html', {'form': form})

def register_view(request):
    return render(request, 'register.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            register = People(
                Login=form.cleaned_data['username'],
                Email=form.cleaned_data['email'],
                Date_birth=form.cleaned_data['date_field']
            )
            register.save()
            return redirect('address_view')
        elif not form.is_valid():
            if not form.cleaned_data.get('username'):
                form.fields['username'].widget.attrs['placeholder'] = 'Не заполнено Имя Пользователя'
                form.fields['username'].widget.attrs['style'] = 'color: red;'
            if not form.cleaned_data.get('email'):
                form.fields['email'].widget.attrs['placeholder'] = 'Не заполнена Почта'
                form.fields['email'].widget.attrs['style'] = 'color: red;'
            if not form.cleaned_data.get('password'):
                form.fields['password'].widget.attrs['placeholder'] = 'Не заполнен Пароль'
                form.fields['password'].widget.attrs['style'] = 'color: red;'
            if not form.cleaned_data.get('date_field'):
                form.fields['date_field'].widget.attrs['placeholder'] = 'Не заполнена Дата Рождения'
                form.fields['date_field'].widget.attrs['style'] = 'color: red;'
        
        return render(request, 'register.html', {'form': form})
    
    else:
        form = RegisterUserForm()
    
    return render(request, 'register.html', {'form': form})
      
def address_view(request):
   return render(request, 'address.html')

def address_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = Address(
                Country = form.cleaned_data['country'],
                City = form.cleaned_data['city'],
                Street = form.cleaned_data['address']
            )
            address.save()
            return redirect('credit_card_view')
        elif not form.is_valid():
            if not form.cleaned_data.get('country'):
                form.fields['country'].widget.attrs['placeholder'] = 'Не заполнена Страна'
                form.fields['country'].widget.attrs['style'] = 'color: red;'
            if not form.cleaned_data.get('city'):
                form.fields['city'].widget.attrs['placeholder'] = 'Не заполнен Город'
                form.fields['city'].widget.attrs['style'] = 'color: red;'
            if not form.cleaned_data.get('address'):
                form.fields['address'].widget.attrs['placeholder'] = 'Не заполнен Адрес'
                form.fields['address'].widget.attrs['style'] = 'color: red;'
        
        return render(request, 'address.html')
    else:
        form = AddressForm()
    
    return render(request, 'address.html', {'form': form})

def credit_card_view(request):
    return render(request, 'credit_card.html')

def credit_card_view(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
           expiration_mouth = form.cleaned_data['expiration_mouth']
           expiration_year = form.cleaned_data['expiration_year']
           expiration_date = f'{expiration_mouth:02d}/{expiration_year:02d}'
    else:
       form = CreditCardForm(request.POST)
    return render(request, 'credit_card.html', {'form': form})


def show(request):
    all_people = People.objects.all()
    return render(request, 'templates/main/main_shop.html', {'people': all_people, 'title': 'Главная Страница'})

def upload(request):
      # Проверяем, загрузил ли пользователь файл.
  if 'file' not in request.FILES:
    # Пользователь не загрузил файл.
    return HttpResponse('No file uploaded.')
  else:
    # Пользователь загрузил файл.
    file = request.FILES['file']
    file_name = str(file.name)
    fs = FileSystemStorage()
    fs.save(os.path.join('uploads/', file_name), file)
    return HttpResponse('File uploaded successfully.')
    
class LoginUser(People, LoginView):
   form_class = AuthenticationForm 
   template_name = 'templates/main/login.html'
   
   def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(**kwargs)
       c_def = self.get_user_context(title = "Авторизация")
       return dict(list(context.items()) + list(c_def.items()))

class RegisterUser(People, CreateView):
   form_class = UserCreationForm
   template_name = 'templates/main/register.html'
#    succes_url = reserve_lazy('login')
   
   def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(**kwargs)
       c_def = self.get_user_context(title = "Регистрация")
       return dict(list(context.items()) + list(c_def.items()))

def people_login_view(request):
   login_data = People.objects.values('Login')
   return render(request, 'login.html', 'register.html', {'login': login_data})

def people_email_view(request):
   email_data = People.objects.values('Email')
   return render(request, 'register.html', {'email': email_data})

# Ручной Views.py для Serializers.py

# class AddressApi(APIView):
    # def get(self, request):
        # lst = Address.objects.all()
        # serializer = ASerializer(lst, many=True)
        # return Response({'Address': serializer.data})
#    
    # def post(self, request):
        # serializer = ASerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({'Address': serializer.data})
#    
    # def put(self, request, pk=None):
        # try:
            # instance = Address.objects.get(pk=pk)
        # except Address.DoesNotExist:
            # return Response({"error": "No object"})
    #   
        # serializer = ASerializer(instance, data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({"address": serializer.data})
# 
    # def delete(self, request, pk=None):
        # try:
            # instance = Address.objects.get(pk=pk)
        # except Address.DoesNotExist:
            # return Response({"error": "No object"})
        # 
        # instance.delete()
        # return Response(status=204)
# 
# class PeopleApi(APIView):
    # def get(self, request):
        # lst = People.objects.all()
        # serializer = PeopleSerializer(lst, many=True)
        # return Response({'People': serializer.data})
    # 
    # def post(self, request):
        # serializer = PeopleSerializer(lst, many=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({'People': serializer.data})
    # 
    # def delete(self, request, pk=None):
        # try:
            # instance = People.objects.get(pk=pk)
        # except People.DoesNotExist:
            # return Response({"error": "No object"})
        # 
        # instance.delete()
        # return Response(status=204)
# 
# class CategoryApi(APIView):
    # def get(self, request):
        # lst = Category.objects.all()
        # serializer = CSerializer(lst, many=True)
        # return Response({'Category': serializer.data})
#    
    # def post(self, request):
        # serializer = CSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({'Category': serializer.data})
#    
    # def delete(self, request, pk=None):
        # try:
            # instance = Category.objects.get(pk=pk)
        # except Category.DoesNotExist:
            # return Response({"error": "No object"})
        # 
        # instance.delete()
        # return Response(status=204)
# 
# class StoreApi(APIView):
    # def get(self, request):
        # lst = Store.objects.all()
        # serializer = SSerializer(lst, many=True)
        # return Response({'Store': serializer.data})
#    
    # def post(self, request):
        # serializer = SSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({'Store': serializer.data})
#    
    # def delete(self, request, pk=None):
        # try:
            # instance = Store.objects.get(pk=pk)
        # except Store.DoesNotExist:
            # return Response({"error": "No object"})
        # 
        # instance.delete()
        # return Response(status=204)
# 
# class ProductApi(APIView):
    # def get(self, request):
        # lst = Product.objects.all()
        # serializer = PSerializer(lst, many=True)
        # return Response({'Product': serializer.data})
#    
    # def post(self, request):
        # serializer = PSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({'Product': serializer.data})
#    
    # def delete(self, request, pk=None):
        # try:
            # instance = Product.objects.get(pk=pk)
        # except Product.DoesNotExist:
            # return Response({"error": "No object"})
        # 
        # instance.delete()
        # return Response(status=204)

class AddressAPIList(generics.ListCreateAPIView):
   queryset = Address.objects.all()
   serializer_class = ASerializer
class AddressAPIUpdate(generics.UpdateAPIView):
   queryset = Address.objects.all()
   serializer_class = ASerializer
class AddressDetailsView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Address.objects.all()
   serializer_class = ASerializer

class PeopleAPIList(generics.ListCreateAPIView):
   queryset = People.objects.all()
   serializer_class = PeopleSerializer
class PeopleAPIUpdate(generics.UpdateAPIView):
   queryset = People.objects.all()
   serializer_class = PeopleSerializer
class PeopleDetailsView(generics.RetrieveUpdateDestroyAPIView):
   queryset = People.objects.all()
   serializer_class = PeopleSerializer

class CategoryAPIList(generics.ListCreateAPIView):
   queryset = Category.objects.all()
   serializer_class = CSerializer
class CategoryAPIUpdate(generics.UpdateAPIView):
   queryset = Category.objects.all()
   serializer_class = CSerializer
class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = CSerializer

class StoreAPIList(generics.ListCreateAPIView):
   queryset = Store.objects.all()
   serializer_class = SSerializer
class StoreAPIUpdate(generics.UpdateAPIView):
   queryset = Store.objects.all()
   serializer_class = SSerializer
class StoreDetailsView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Store.objects.all()
   serializer_class = SSerializer

class ProductAPIList(generics.ListCreateAPIView):
   queryset = Product.objects.all()
   serializer_class = PSerializer
class ProductAPIUpdate(generics.UpdateAPIView):
   queryset = Product.objects.all()
   serializer_class = PSerializer
class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Product.objects.all()
   serializer_class = PSerializer