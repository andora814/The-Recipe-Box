from rest_framework import serializers
from .models import Recipe, RecipeIngredient

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_ingredients = serializers.HyperlinkedRelatedField(
        view_name='recipe_ingredient_detail',
        many=True,
        read_only=True
    )

    recipe_url = serializers.ModelSerializer.serializer_url_field(view_name='recipe_detail')

    class Meta:
        model = Recipe
        fields = ('id', 'recipe_url', 'title', 'ready_in_minutes', 'servings', 'source_url', 'image', 'summary', 'source', 'recipe_ingredients',)

class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(
        view_name='recipe_detail',
        read_only=True
    )
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(),
        source='recipe'
    )
    recipe_ingredient_url = serializers.ModelSerializer.serializer_url_field(view_name='recipe_ingredient_detail')

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'recipe_ingredient_url', 'name', 'quantity', 'unit', 'recipe', 'recipe_id')