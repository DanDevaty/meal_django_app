from django.db import models
from datetime import timedelta
from users.models import CustomUser
from ingredients.models import Ingredient


class Recipe(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    instructions = models.TextField("Instructions")
    category = models.CharField("Category", max_length=50)
    preparation_time = models.DurationField("Preparation Time", help_text="Preparation time (HH:MM)")
    servings = models.IntegerField("Servings")
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    ingredients = models.ManyToManyField('ingredients.Ingredient', related_name="recipes")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def formatted_preparation_time(self):
        if self.preparation_time:
            total_seconds = int(self.preparation_time.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            return f"{hours} h {minutes} min"
        return "unknown"
