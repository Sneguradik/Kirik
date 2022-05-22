from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageRender, name='Home'),
    path('Category/<int:category>/', CategoryFilter, name='Category'),
    path('Recipe/<int:recipe>/', SingleRecipe, name='SingleRecipe'),
    path('OfferRecipe/', OfferRecipe, name='OfferRecipe'),
]