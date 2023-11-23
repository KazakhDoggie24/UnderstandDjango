from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'register-input', 'placeholder': 'Название логина...'}), required=True)
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'register-input', 'placeholder': 'Почта...'}), required=True)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'register-input', 'placeholder': 'Пароль...'}), required=True)
    date_field = forms.DateField(
        label='', widget=forms.DateInput(attrs={'type': 'date', 'class': 'register-input', 'placeholder': 'Дата рождения...'}), required=True)
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким логином уже существует.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с такой почтой уже существует.")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if User.objects.filter(password=password).exists():
            raise forms.ValidationError("Пользователь с таким паролем уже существует.")
        return password

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'login-input', 'placeholder': 'Введите логин...'}), required=True)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'login-input', 'placeholder': 'Введите пароль...'}), required=True)

class AddressForm(forms.Form):
    country = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'address-input', 'placeholder': 'Введите страну...'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'address-input', 'placeholder': 'Введите город...'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'address-input', 'placeholder': 'Введите адрес...'}))

class CreditCardForm(forms.Form):
    card_owner = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'cc-input', 'placeholder': 'Владелец карты...', 'style':'text_transform: uppercase;', 'pattern': '[A-Z]*'}))
    card_number = forms.IntegerField(label='', widget=forms.TextInput(attrs={
        'class': 'cc-input', 'placeholder': 'Номер карты...', 'pattern': '[0-9]{16}', 'maxlength': '16'}))
    expiration_month = forms.IntegerField(label='', min_value=1, max_value=12, widget=forms.NumberInput(attrs={
        'class': 'exp-date-input', 'min': '1', 'max': '12', 'maxlength': '2', 'placeholder': 'М..'}))
    expiration_year = forms.IntegerField(label='', min_value=0, max_value=99, widget=forms.NumberInput(attrs={
        'class': 'exp-date-input', 'min': '0', 'max': '99', 'maxlength': '2', 'placeholder': 'Г..'}))
    cvv = forms.IntegerField(label='', min_value=0, max_value=999, widget=forms.NumberInput(attrs={
        'class': 'cvv-input', 'placeholder': 'CVV...', 'step': '1'}))
    
    def clean(self):
        cleaned_data = super().clean()
        expiration_month = cleaned_data.get('expiration_month')
        expiration_year = cleaned_data.get('expiration_year')
        
        if expiration_month is not None and expiration_year is not None:
            expiration_date = f"{expiration_month:02}/{expiration_year:02}"
            cleaned_data['expiration_date'] = expiration_date
        
        return cleaned_data