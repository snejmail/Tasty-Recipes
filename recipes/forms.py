from django import forms

from recipes.models import Recipe


class BaseRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {
            'instructions': forms.Textarea(attrs={
                'placeholder': "Enter detailed instructions here..."
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': "Optional image URL here..."
            }),
            'ingredients': forms.Textarea(attrs={
                'placeholder': "ingredient1, ingredient2, ..."
            }),
        }
        help_texts = {
            'ingredients': "Ingredients must be separated by a comma and space.",
            'cooking_time': "Provide the cooking time in minutes.",
        }


class RecipeForm(BaseRecipeForm):
    pass


class DeleteRecipeForm(BaseRecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
