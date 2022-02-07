from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipeingredients/', views.RecipeIngredientList.as_view(), name='recipe_ingredient_list'),
    path('recipeingredients/<int:pk>', views.RecipeIngredientDetail.as_view(), name='recipe_ingredient_detail'),
]