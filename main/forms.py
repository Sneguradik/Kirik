from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import Textarea
from .models import *

class OfferRecipeForm(forms.Form):
    title = forms.CharField(max_length=255 , widget=forms.TextInput(attrs={"class":"form-control"}))
    ingredients = forms.CharField(widget=Textarea(attrs={"class":"form-control"}),help_text='ingredient_name ingredient_amount ingredient_unit')
    short_description = forms.CharField(max_length=255 , widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(widget=Textarea(attrs={"class":"form-control"}))
    video = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class":"form-select"}))

class Search(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), required=False)
    category = forms.ModelChoiceField(required=False,queryset=Category.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))