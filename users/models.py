from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def first_letter_validator(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")


class Profile(models.Model):

    nickname = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2),],
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'min_length': "Nickname must be at least 2 chars long!",
        }
    )
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[first_letter_validator],
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[first_letter_validator],
    )
    chef = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nickname





