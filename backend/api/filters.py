from django_filters import AllValuesMultipleFilter
from django_filters.rest_framework import FilterSet, filters
from django_filters.widgets import BooleanWidget

from recipes.models import Ingredient, Recipe


class IngredientSearchFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='startswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    author = AllValuesMultipleFilter(field_name="author__id")
    tags = AllValuesMultipleFilter(field_name="tags__slug")
    is_in_shopping_cart = filters.BooleanFilter(widget=BooleanWidget())
    is_favorited = filters.BooleanFilter(widget=BooleanWidget())

    class Meta:
        model = Recipe
        fields = ["author", "tags",
                  "is_favorited", "is_in_shopping_cart"]
