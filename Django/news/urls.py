from django.urls import path, re_path, include
from rest_framework import routers
from . import views

app_name = 'news'

router = routers.DefaultRouter()
router.register(r'column', views.ColumnViewSet)
router.register(r'article', views.ArticleViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'column/(?P<column_slug>[^/]+)/$', views.column_detail, name='column'),
    re_path(r'article/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', views.article_detail, name='article'),
    path(r'api/', include(router.urls)),
    re_path(r'column/(?P<id>[^/]+)/$', views.ColumnList.as_view(), name='column'),
    re_path(r'column2/', views.ColumnList2.as_view(), name='column'),
]
