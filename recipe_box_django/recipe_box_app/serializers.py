from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_ingredients = serializers.HyperlinkedRelatedField(
        view_name='recipe_ingredient_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ready_in_minutes', 'servings', 'source_url', 'image', 'summary', 'source', 'recipe_ingredients',)

class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(
        view_name='recipe_detail',
        read_only=True
    )
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(),
        source='recipe'
    )

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'quantity', 'unit', 'recipe', 'recipe_id')