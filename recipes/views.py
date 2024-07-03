from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from recipes.forms import RecipeForm, DeleteRecipeForm
from recipes.models import Recipe
from users.models import Profile


def catalogue(request):
    profile = Profile.objects.first()
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
        'profile_exists': True if profile else False,
        'profile_id': profile.id if profile else None,
    }

    return render(request, 'catalogue.html', context)


def create_recipe(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'create-recipe.html', context)


def details_recipe(request, pk):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass

    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.split(', ')
    recipe_pic = recipe.image_url

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'profile': profile,
        'recipe_pic': recipe_pic,
    }

    return render(request, 'details-recipe.html', context)


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'edit-recipe.html', context)


def delete_recipe(request, pk):
    profile_exists = Profile.objects.exists()

    if not profile_exists:
        return redirect('create_profile')

    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogue')

    form = DeleteRecipeForm(instance=recipe)
    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'delete-recipe.html', context)