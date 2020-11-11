from django.urls import path, include
from . views import *
urlpatterns = [
    path('', ArticleAPIView.as_view(), name='article_api'),
    path('detail/<int:id>/', ArticleDetail.as_view(), name='article_detail'),
    path('generic/article/<int:id>/',
         GenericApiView.as_view(), name='generic_api'),


]
