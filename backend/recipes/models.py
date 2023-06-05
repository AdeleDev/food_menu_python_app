from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='favorites_user', )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        verbose_name='Recipe',
        related_name='favorites', )

    class Meta:
        verbose_name = 'Favorites'
        constraints = [models.UniqueConstraint(fields=['user', 'recipe'],
                                               name='unique_favorite')]


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='shopping_list', )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        verbose_name='Recipe',
        related_name='shopping_list', )

    class Meta:
        verbose_name = 'Shopping list'
        constraints = [models.UniqueConstraint(fields=['user', 'recipe'],
                                               name='unique_basket')]


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Ingredient Title',
        max_length=200, )
    measurement_unit = models.CharField(
        verbose_name='Units',
        max_length=200, )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ingredient'
        verbose_name_plural = 'General ingredients amount'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Title',
        max_length=200,
        unique=True, )
    color = models.CharField(
        verbose_name='Color HEX code',
        max_length=7,
        unique=True,
        validators=(
            RegexValidator(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'),
        )
    )
    slug = models.SlugField(
        verbose_name='Label',
        unique=True,
        max_length=200,
    )

    class Meta:
        verbose_name = 'Tag'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='recipes', )
    name = models.CharField(
        verbose_name='Recipe title',
        max_length=200,
         )
    image = models.ImageField(
        'Recipe image',
        upload_to='recipes/', )
    text = models.TextField(
        verbose_name='Recipe description', )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient')
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Tags',
        related_name='recipes', )
    cooking_time = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Cooking time',
        validators=(
            MinValueValidator(
                1, message='Cooking time must be at least 1 minute'),),
    )
    pub_date = models.DateTimeField(
        verbose_name='Pub date',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Recipe'
        ordering = ('-pub_date',)

    def __str__(self):
        return f'{self.name}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Ingredients in recipe')
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        max_length=200,
        verbose_name='Ingredient')
    amount = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Ingredient amount',
        validators=(
            MinValueValidator(
                1, message='Amount must be at least 1'),),
    )

    class Meta:
        default_related_name = 'ingredients_recipe'
        verbose_name = 'Ingredient amount'

    def __str__(self):
        return f'{self.ingredient}'
