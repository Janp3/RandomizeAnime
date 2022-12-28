from django import forms
from django.db import models

# Create your models here.


class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)


class Animes (models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, default=None)


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Animes
        fields = "__all__"
