from django.shortcuts import render, redirect, get_object_or_404

from common.views import get_first_profile
from recipes.models import Recipe
from users.forms import ProfileForm, EditProfileForm, DeleteProfileForm
from users.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {'form': form}
    return render(request, 'create-profile.html', context)


def details_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    published_recipes_count = Recipe.objects.filter(author=profile).count()
    context = {
        'profile': profile,
        'published_recipes_count': published_recipes_count,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details_profile', profile_id=profile.id)
    context = {'form': form}
    return render(request, 'edit-profile.html', context)


def delete_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        profile.delete()
        return redirect('home_page')
    context = {'form': DeleteProfileForm(instance=profile)}
    return render(request, 'delete-profile.html', context)

