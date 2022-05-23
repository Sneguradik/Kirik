from django.shortcuts import render,redirect
from .models import Category, Recipe,Ingredient
from django.core.paginator import Paginator
from .forms import SearchForm, UserRegisterForm, OfferRecipeForm, UserLoginForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q

def HomePageRender(request):
    Recipes = Recipe.objects.filter(status = 'published')
    paginator = Paginator(Recipes, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    Categories = Category.objects.all()
    return render( request, 'main/HomePage.html', {'page_obj': page_obj, 'category': Categories } )

def CategoryFilter(request, category):
    Recipes = Recipe.objects.filter(status = 'published', category = category)
    paginator = Paginator(Recipes, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    Categories = Category.objects.all()
    return render( request, 'main/HomePage.html', {'page_obj': page_obj, 'category': Categories } )

def SingleRecipe(request, recipe):
    Recipes = Recipe.objects.get(pk=recipe)
    return render(request, 'main/Recipe.html', {'recipe': Recipes})

def OfferRecipe(request):
    if request.method == 'POST':
        form = OfferRecipeForm(request.POST)
        if form.is_valid():
            link = 'https://www.youtube.com/embed/'
            f=-1
            new = ''
            while form.cleaned_data['video'][f]!='/':
                new= new + form.cleaned_data['video'][f]
                f-=1 
            link = link+new[::-1]
            ing = form.cleaned_data['ingredients'].split()
            s = []
            print(ing, len(ing))
            for i in range(0,len(ing),3):
                d= {'name': ing[i] ,'amount' : int(ing[i+1]), 'units' : ing[i+2]}
                Ingredient.objects.create(**d)
                s.append(d)
            data={
                'title': form.cleaned_data['title'],
                'short_description': form.cleaned_data['short_description'],
                'description': form.cleaned_data['description'],
                'video': link,
                'category': form.cleaned_data['category'],
                'author': request.user
            }
            Recipe.objects.create(**data)
            rec =Recipe.objects.get(title = data['title'])
            for el in s:
                rec.ingredients.add(Ingredient.objects.filter(**el)[0])
        return redirect('Home')
    else:
        form = OfferRecipeForm()
    return render(request, 'main/OfferRecipe.html', {'form': form})
    
def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1']==form.cleaned_data['password2']:
                user = form.save()
                login(request, user)
                messages.success(request, 'Вы успешно зарегистрировались')
                return redirect('Login')
            else:
                messages.error(request, 'Ошибка регистрации')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/Register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли')
            return redirect('Home')
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = UserLoginForm()
    return render(request, 'main/Login.html',  {'form':form})

def Logout(request):
    logout(request)
    return redirect('Login')

def Search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            
            
            qr = form.cleaned_data['search'].split()
            res = list()
            if form.cleaned_data['category']==None:
                category = Category.objects.all()
            else:
                category=[form.cleaned_data['category']]
            if qr != []:
                for i in qr:
                    
                    a = Recipe.objects.filter(Q(title__icontains= i) | Q(short_description__icontains = i) | Q(description__icontains= i) , category__in= category, status='published')
                    res.append(*a)
            else:
                res= Recipe.objects.filter(Subject__in= category, Status='published')
            return render( request, 'main/searchresult.html', {'recipes':res} )
    else:
        form = SearchForm()
        return render(request, 'main/Search.html', {'form': form})