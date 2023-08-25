from django.urls import path
from .views import (
    HomePageView,
    ArticleListView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("articles/", ArticleListView.as_view(), name="article_list"),
]