from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Article
from .views import *

# Model Tests
class ArticleModelTest(TestCase):

    def test_create_article(self):
        author = get_user_model().objects.create_user(username="testuser", password="password")
        article = Article.objects.create(
            title="Test Model",
            date=timezone.now(),
            content="Example content",
            author=author,
        )

        self.assertEqual(article.title, "Test Model")
        self.assertEqual(article.author, author)

    def test_get_absolute_url(self):
        author = get_user_model().objects.create_user(username="testuser", password="password")
        article = Article.objects.create(
            title="Test Model",
            date=timezone.now(),
            content="Example content",
            author=author,
        )

        expected_url = reverse("article_detail", args=[str(article.id)])
        actual_url = article.get_absolute_url()
        
        self.assertEqual(expected_url, actual_url)

