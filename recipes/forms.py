from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "user",
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "meal_type",
            "cuisine_type",  # Corrected field name
            "calories",
        ]
        widgets = {
            "instructions": RichTextWidget(),
            "ingredients": RichTextWidget(),
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            "meal_type": "Meal Type",
            "cuisine_type": "Cuisine Type",  # Corrected field name
            "calories": "Calories",
        }
