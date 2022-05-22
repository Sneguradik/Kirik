from django.shortcuts import render,redirect
from .models import Category, Recipe,Ingredient
from django.core.paginator import Paginator
from .forms import UserRegisterForm, OfferRecipeForm, UserLoginForm, UserCreationForm

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
            while s!='/':
                new= new + form.cleaned_data['video'][f]
                f-=1 
            link = link+new[::-1]
            ing = form.cleaned_data['ingredients'].split()
            s = []
            for i in range(0,len(ing),len(ing)/3):
                d= {'name': ing[i] ,'amount' : ing[i+1], 'unit' : ing[i+2]}
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
                rec.ingredients.add(Ingredient.objects.filter(**d)[0])
        return redirect('Home')
    else:
        form = OfferRecipeForm()
    return render(request, 'main/OfferRecipe.html', {'form': form})
    