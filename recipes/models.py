from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from users.models import Profile


class Recipe(models.Model):
    class Meta:
        db_table = 'recipes_recipe'  # Or the actual name of your table

    CUISINE_TYPE_CHOICES = (
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other'),
    )
    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(10),],
    )
    cuisine_type = models.CharField(
        null=False,
        blank=False,
        max_length=7,
        choices=CUISINE_TYPE_CHOICES,
    )
    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space.",
    )
    instructions = models.TextField(
        null=False,
        blank=False,
    )
    cooking_time = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1),],
        help_text="Provide the cooking time in minutes.",
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
    )

    def __str__(self):
        return self.title
