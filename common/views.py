from django.shortcuts import render, redirect

from recipes.models import Recipe
from users.models import Profile


def get_first_profile():
    return Profile.objects.first()


def home_page(request):
    profile_exists = Profile.objects.exists()
    if not profile_exists:
        return redirect('create_profile')
    return redirect('catalogue')