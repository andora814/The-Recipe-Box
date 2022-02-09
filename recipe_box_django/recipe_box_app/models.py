from django.db import models

class Recipe(models.Model):
  title = models.CharField(max_length=100)
  ready_in_minutes = models.IntegerField()
  servings = models.IntegerField()
  source_url = models.TextField(blank=True)
  image = models.TextField()
  summary = models.TextField()
  instructions = models.TextField(default="no instructions")

  def __str__(self):
    return self.title

class Ingredient(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class RecipeIngredient(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_ingredients')
  name =  models.CharField(max_length=100)
  quantity = models.CharField(max_length=100)
  unit = models.CharField(max_length=100)

  def __str__(self):
    return self.name