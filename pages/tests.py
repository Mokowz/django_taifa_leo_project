from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

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

