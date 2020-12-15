from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.
class Recipe(TimeStampedModel):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)


	def __str__(self):
		return f"{self.title}\t {self.created}"