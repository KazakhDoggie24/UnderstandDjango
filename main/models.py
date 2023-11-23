# Create your models here.

from django.db import models
from django.contrib.auth.hashers import make_password

class Address(models.Model):
    Country = models.CharField(max_length = 100)
    City = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)

class People(models.Model):
    Login = models.CharField(max_length=50, unique=True, default='')
    Email = models.EmailField(unique=True)
    Date_birth = models.DateField(auto_now_add=True)
    File = models.FileField(upload_to='templates/main', default='default_file.png')
    Address = models.ForeignKey(Address, on_delete = models.CASCADE, default='')

    print_print = models.CharField(max_length=100, choices=(
        ('Login','login'),
        ('Email', 'email')))
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return self.password(raw_password, self.password)

    def __str__(people):
        if people.print_print in 'Login' and 'Email' or 'login' and 'email':
            return f"{people.Login} - {people.Email}"

class CreditCard(models.Model):
    CreditCardNumber = models.CharField(max_length=16)
    CardholderName = models.CharField(max_length=50)
    ExpirationDate = models.DateField(max_length=5)
    People = models.ForeignKey(People, on_delete=models.CASCADE)

class Category(models.Model):
    CategoryName = models.CharField(max_length=50)

    def __str__ (category):
        return category.CategoryName
class Store(models.Model):
    StoreName = models.CharField(max_length=50)
    StoreAddress = models.CharField(max_length=100)
    StoreContact = models.CharField(max_length=100)
    StoreDescription = models.TextField()

    print_print = models.CharField(max_length=100, choices=(
        ('Name', 'name'),
        ('Address', 'address'),
        ('Contact', 'contact'),
        ('Description', 'description')))
    
    def __str__(store):
        print_print_lower = store.print_print.lower()
        if store.print_print == 'Name' or print_print_lower == 'name':
            return store.StoreName
        elif store.print_print == 'Address' or print_print_lower == 'address':
            return store.StoreAddress
        elif store.print_print == 'Contact' or print_print_lower == 'contact':
            return store.StoreContact
        elif store.print_print == 'Description' or print_print_lower == 'description':
            return store.StoreDescription
        else:
            return "Invalid request!"
    
class Product(models.Model):
    ProductName = models.CharField(max_length=50)
    ProductDescription = models.TextField()
    Price = models.DecimalField(max_digits=8, decimal_places=2)
    Date = models.DateTimeField(auto_now_add=True)
    ProductCompany = models.CharField(max_length=50)
    Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    print_print = models.CharField(max_length=100, choices=(
        ('Name', 'name'),
        ('Description', 'description'),
        ('Price', 'price'),
        ('Date', 'date'),
        ('Company','company')),
        default='')

    def __str__(product):
        print_print_lower = product.print_print.lower()
        if product.print_print == 'Name' or print_print_lower == 'name':
            return product.ProductName
        elif product.print_print == 'Description' or print_print_lower == 'description':
            return product.ProductDescription
        elif product.print_print == 'Price' or print_print_lower == 'price':
            return str(product.Price)
        elif product.print_print == 'Date' or print_print_lower == 'date':
            return str(product.Date)
        elif product.print_print == 'Company' or print_print_lower == 'company':
            return product.ProductCompany
        else:
            return "Invalid request!"