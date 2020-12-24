from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Tour
from .serializers import RecipeSerializer, TourSerializer

# Create your views here.
class RecipeView(generics.ListAPIView):
	queryset = Recipe.objects.all().order_by('created')
	serializer_class = RecipeSerializer

class TourView(generics.ListAPIView):
	queryset = Tour.objects.all().order_by('created')
	serializer_class = TourSerializer