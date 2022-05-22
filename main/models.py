from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField('Ingredient Name', max_length=255)
    amount = models.IntegerField("Amount")
    units = models.CharField("Units", max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name  = "Ingredient"
        verbose_name_plural = "Ingredients"

class Category(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Recipe(models.Model):
    title = models.CharField("Title", max_length=255)
    ingredients = models.ManyToManyField(Ingredient, verbose_name="Ingredient")
    author= models.ForeignKey(User, models.SET_NULL, verbose_name="Author", null=True)
    short_description = models.CharField('Short Description', max_length=255)
    description = models.TextField("Description")
    video = models.TextField("Video Link")
    category = models.ForeignKey(Category, models.SET_NULL, null=True, verbose_name= "Category")

    OptionsForStatus = [
        ('published', 'Published'),
        ('offered', 'Offered'),
        
    ]
    status = models.CharField(verbose_name='Status', choices=OptionsForStatus, default='offered', max_length=40)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Reciepe"
        verbose_name_plural = "Reciepes"

