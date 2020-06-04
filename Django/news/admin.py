from django.contrib import admin

# Register your models here.
from .models import Column, Article

# 这个只能用在存在一对多的情况下
class ArticleInline(admin.TabularInline):
    model = Article
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'pub_date', 'update_date']

class ColumnAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'intro', 'nav_display', 'home_display']

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
