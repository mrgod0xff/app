from django.contrib import admin

# Register your models here.
from .models import Nouveaute, Categorie, Article


admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Nouveaute)