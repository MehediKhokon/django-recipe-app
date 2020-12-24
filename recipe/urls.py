# from django.contrib import admin
from django.urls import path
from .views import RecipeView, TourView

urlpatterns = [
    path('', RecipeView.as_view()),
    path('api/', TourView.as_view()),
]
