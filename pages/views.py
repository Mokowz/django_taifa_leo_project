from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
)

from .models import Article

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"
