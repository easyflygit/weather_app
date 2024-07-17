from django.test import TestCase, Client
from django.urls import reverse
from .models import SearchHistory
from .utils import get_weather


class WeatherTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_weather(self):
        response = get_weather('London')
        self.assertIsNotNone(response)

    def test_search_history(self):
        city = 'London'
        search, created = SearchHistory.objects.get_or_create(city=city)
        search.search_count += 1
        search.save()
        self.assertEqual(SearchHistory.objects.filter(city=city).count(), 1)

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
