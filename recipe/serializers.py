from rest_framework import serializers
from .models import Recipe, Tour


class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = ['id', 'title', 'description', 'created']

class TourSerializer(serializers.ModelSerializer):
	class Meta:
		models = Tour
		fields = ['id', 'name', 'information', 'image', 'created']