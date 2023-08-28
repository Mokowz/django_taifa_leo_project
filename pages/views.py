from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    DetailView,
)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Article

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class ArticleListView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"
    paginate_by = 2

class ArticleDetailView(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = Article
    template_name = "article_detail.html"

    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Article
    template_name = "article_new.html"
    fields = ["title",  "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    login_url = "login"
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "content"]

    def test_func(self):
        return self.request.user == self.get_object().author

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    login_url = "login"
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        return self.request.user == self.get_object().author