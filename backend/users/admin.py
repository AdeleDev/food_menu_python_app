from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.models import Group

from .models import Follow, User


@register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name'
    )
    search_fields = ('username', 'email')
    empty_value_display = '-empty-'
    list_filter = ('email', 'username')


@register(Follow)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author'
    )
    search_fields = ('user',)


admin.site.unregister(Group)
