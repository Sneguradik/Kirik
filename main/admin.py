from django.contrib import admin
from .models import Ingredient, Recipe, Category

class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", 'amount', 'units']
    list_filter = [ "units"]
    search_fields = ["name"]

class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "category","author", 'status']
    list_filter = ["category",'status']
    list_display_links = ['title']
    search_fields = ['title', 'author', 'category' , 'short_description','description']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Category, CategoryAdmin)