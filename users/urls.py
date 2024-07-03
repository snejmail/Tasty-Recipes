from django.urls import path
from users.views import create_profile, details_profile, edit_profile, delete_profile

urlpatterns = [
    path('profile/create/', create_profile, name='create_profile'),
    path('profile/details/<int:profile_id>/', details_profile, name='details_profile'),
    path('profile/edit/<int:profile_id>/', edit_profile, name='edit_profile'),
    path('profile/delete/<int:profile_id>/', delete_profile, name='delete_profile'),
]
