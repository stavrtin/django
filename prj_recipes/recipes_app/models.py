from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return f'Автор рецепта: {self.name}.Возраст {self.age}'

class Category(models.Model):
    categ_name = models.CharField(max_length=100)
    categ_description = models.CharField(max_length=100)
    categ_img = models.ImageField()

    def __str__(self):
        return f'Категория: {self.categ_name}'

class Recipe(models.Model):
    rec_name = models.CharField(max_length=100)
    rec_description = models.CharField(max_length=100)
    rec_time = models.IntegerField()
    rec_img = models.ImageField()
    rec_author = models.ForeignKey(User, on_delete=models.CASCADE)
    # rec_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rec_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Ingredients(models.Model):
    ingr_name = models.CharField(max_length=100)
    ingr_amount = models.FloatField()
    ingr_unit = models.CharField(max_length=50)
    ingr_rec = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ингредиент: {self.ingr_name}'

class Step(models.Model):
    step_number = models.IntegerField()
    step_text = models.TextField()
    step_rec = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'Этап рецепта: {self.step_number} -  {self.step_text}'
