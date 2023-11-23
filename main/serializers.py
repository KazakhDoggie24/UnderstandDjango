from rest_framework import serializers
from .models import Address, People, Category, Store, Product
from django.contrib.auth.hashers import make_password

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Ручной метод Serializers

# class AddressModel:
    # def __init__(self, city, street):
        # self.city = city
        # self.street = street
# 
# class ASerializer(serializers.ModelSerializer):
    # city = serializers.CharField(max_length=255)
    # street = serializers.CharField(max_length=255)
    # class Meta:
        # model = Address
        # fields = ('city', 'street')
    # 
    # def create(self, validated_data):
        # return Address.objects.create(**validated_data)
    # 
    # def update(self, instance, validated_data):
        # instance.city = validated_data.get('city', instance.city)
        # instance.street = validated_data.get('street', instance.street)
        # instance.save()
        # return instance
        # 
# class PeopleSerializer(serializers.ModelSerializer):
    # login = serializers.CharField(max_length=255)
    # password = serializers.CharField(write_only=True)
    # email = serializers.EmailField(max_length=255)
    # date_birth = serializers.DateField(format='%d/%m/%y')
    # class Meta:
        # model = People
        # fields = ('login', 'password', 'email', 'date_birth')
    # 
    # def create(self, validated_data):
        # password = validated_data.pop('password')
        # instance = People(**validated_data)
        # instance.set_password(password)
        # instance.save()
        # return instance
    # 
    # def update(self, instance, validated_data):
        # instance.login = validated_data.get('login', instance.login)
        # instance.email = validated_data.get('email', instance.email)
        # instance.data_birth = validated_data.get('data_birth', instance.data_birth)
# 
        # password = validated_data.get('password')
        # if password:
            # instance.set_password(password)
# 
        # instance.save()
        # return instance
    # 
    # def delete(self, instance):
        # instance.delete()
# 
# class CSerializer(serializers.ModelSerializer):
    # CategoryName = serializers.CharField(max_length=50)
    # class Meta:
        # model = Category
        # fields = ('CategoryName',)
# 
    # def create(self, validated_data):
        # return Category.objects.create(**validated_data)
    # 
    # def update(self, instance, validated_data):
        # instance.CategoryName = validated_data.get('CategoryName', instance.CategoryName)
        # instance.save()
        # return instance
# 
# class SSerializer(serializers.ModelSerializer):
    # store_name = serializers.CharField(max_length=50)
    # address = serializers.CharField(max_length=100)
    # contact = serializers.CharField(max_length=100)
    # description = serializers.DictField()
    # class Meta:
        # model = Store
        # fields = ('store_name', 'address', 'contact', 'description')
# 
    # def create(self, validated_data):
        # return Store.objects.create(**validated_data)
    # 
    # def update(self, instance, validated_data):
        # instance.store_name = validated_data.get('store_name', instance.store_name)
        # instance.address = validated_data.get('address', instance.address)
        # instance.contact = validated_data.get('contact', instance.contact)
        # instance.description = validated_data.get('description', instance.description)
        # instance.save()
        # return instance
# 
# class PSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Product
        # fields = ('name', 'description', 'price', 'date', 'company')
    # 
    # def create(self, validated_data):
        # return Product.objects.create(**validated_data)
    # 
    # def update(self, instance, validated_data):
        # instance.name = validated_data.get('name', instance.name)
        # instance.description = validated_data.get('description', instance.description)
        # instance.price = validated_data.get('price', instance.price)
        # instance.date = validated_data.get('date', instance.date)
        # instance.company = validated_data.get('company', instance.company)
        # instance.save()
        # return instance

class ASerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"

class CSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"