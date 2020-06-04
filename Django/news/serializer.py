from rest_framework import serializers
from .models import Column, Article

class ColumnSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Column
        fields = '__all__'
        # fields = ('name', 'slug', 'intro', 'nav_display', 'home_display')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title', 'slug', 'author', 'content', 'published', 'pub_date', 'update_date')