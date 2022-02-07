from django.contrib import admin

from django.contrib import admin
from .models import Recipe
from .models import Instruction
from .models import Ingredient
from .models import RecipeIngredient

admin.site.register(Recipe)
admin.site.register(Instruction)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
