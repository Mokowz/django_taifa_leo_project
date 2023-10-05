from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Article
from .views import *

# Model Tests
class ArticleModelTest(TestCase):
    def setUp(self):
        self.author = get_user_model().objects.create_user(
            username="testuser", 
            password="password"
        )
        self.article = Article.objects.create(
            title="Test Model",
            date=timezone.now(),
            content="Example content",
            author=self.author,
        )

    def test_create_article(self):
        self.assertEqual(self.article.title, "Test Model")
        self.assertEqual(self.article.author, self.author)

    def test_get_absolute_url(self):

        expected_url = reverse("article_detail", args=[str(self.article.id)])
        actual_url = self.article.get_absolute_url()
        
        self.assertEqual(expected_url, actual_url)

    def test_str_method(self):

        self.assertEqual(self.article.__str__(), "Test Model")


# Test the update view
class ArticleUpdateViewTest(TestCase):
    def setUp(self):
        self.author = get_user_model().objects.create_user(
            username="testuser", 
            password="password"
        )
        self.article = Article.objects.create(
            title="Test Model",
            date=timezone.now(),
            content="Example content",
            author=self.author,
        )

    def test_update_by_author_redirect(self):
        self.client.login(username="testuser", password="password")

        response = self.client.post(
            f'/articles/{self.article.pk}/edit/',
            {"title": "Updated Title",
             "content": "Updated Content"
             }
        )

        # Test user was redirected to the detail view
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/articles/{self.article.pk}/")


    def test_author_is_user(self):
        self.clien


