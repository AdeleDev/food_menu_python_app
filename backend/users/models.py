from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from rest_framework.exceptions import ValidationError


def validate_me(value):
    if value in settings.BLACK_USERNAME_LIST:
        raise ValidationError('Username is in stop-list')


class User(AbstractUser):
    username = models.CharField(
        verbose_name='User name',
        max_length=150,
        unique=True,
        validators=(RegexValidator(regex=r'^[\w.@+-]+\Z'), validate_me,)
    )
    first_name = models.CharField(
        verbose_name='Name',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Surname',
        max_length=150,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ('email',)
        verbose_name = 'User'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Subscriber',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Author',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Subscription'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follow',
            )
        ]
