from django.contrib import admin

from .models import Animes, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Animes)
class AnimeAdmin(admin.ModelAdmin):
    ...
