from django.test import TestCase
from django.urls import reverse
from .models import SearchHistory
from .utils import get_weather
from django.contrib.auth.models import User


class WeatherTests(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_search_history_creation(self):
        # Создаем объект SearchHistory с корректным user
        search_history = SearchHistory.objects.create(
            user=self.user,
            city='London',
            search_count=0
        )
        self.assertEqual(search_history.user, self.user)
        self.assertEqual(search_history.city, 'London')
        self.assertEqual(search_history.search_count, 0)

    def test_search_history(self):
        city = 'London'
        search, created = SearchHistory.objects.get_or_create(city=city, user=self.user)
        search.search_count += 1
        search.save()
        self.assertEqual(SearchHistory.objects.filter(city=city).count(), 1)

    def test_get_weather(self):
        response = get_weather('London')
        self.assertIsNotNone(response)

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_index_view(self):
        url = reverse('index')
        data = {'city': 'London'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('weather', response.context)
