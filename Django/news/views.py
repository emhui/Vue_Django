from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Column, Article

from rest_framework import viewsets, generics
from .serializer import ArticleSerializer, ColumnSerializer

# Create your views here.

def index(request):
    home_display_columns = Column.objects.filter(home_display = True)
    nav_display_columns = Column.objects.filter(nav_display = True)
    return render(request, 'index.html', {'home_display_columns': home_display_columns, 'nav_display_columns': nav_display_columns})

def column_detail(request, column_slug):
    column = Column.objects.get(slug = column_slug)
    return render(request, 'news/column.html', context={
        'column': column
    })
    # return HttpResponse('column_slug' + column_slug)
    
def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    # article = Article.objects.filter(slug=article_slug)
    if article_slug != article.slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', context={
        'article': article
    })
    # return HttpResponse('article_slug' + article_slug)

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ColumnList(generics.ListAPIView):
    serializer_class = ColumnSerializer
    
    # 重写这个方法可以自定义查询
    def get_queryset(self):
        id = self.kwargs['id']
        return Column.objects.filter(id=id)

class ColumnList2(generics.ListAPIView):
    serializer_class = ColumnSerializer
    
    def get_queryset(self):
        queryset = Column.objects.all()
        id = self.request.query_params.get('id')
        slug = self.request.query_params.get('slug')

        if id is not None:
            queryset = queryset.filter(id = id)
        if slug is not None:
            queryset = queryset.filter(slug=slug)

        return queryset