from django.urls import path, include

from recipes.views import catalogue
from recipes.views import create_recipe, details_recipe, edit_recipe, delete_recipe

urlpatterns = [
    path('catalogue/', catalogue, name="catalogue"),
    path('create/', create_recipe, name='create_recipe'),
    path('<int:pk>/', include([
        path('details/', details_recipe, name='details_recipe'),
        path('edit/', edit_recipe, name='edit_recipe'),
        path('delete/', delete_recipe, name='delete_recipe'),
    ]))
]
