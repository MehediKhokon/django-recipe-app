from django.shortcuts import render
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.
class RecipeView(generics.ListAPIView):
	queryset = Recipe.objects.all().order_by('created')
	serializer_class = RecipeSerializer