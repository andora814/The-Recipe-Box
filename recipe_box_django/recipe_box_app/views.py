from django.shortcuts import render
from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser
from .serializers import RecipeSerializer, RecipeIngredientSerializer, IngredientSerializer, InstructionSerializer
from .models import Recipe, RecipeIngredient, Ingredient, Instruction

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeIngredientList(generics.ListCreateAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

class RecipeIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class InstructionList(generics.ListCreateAPIView):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer

class InstructionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer