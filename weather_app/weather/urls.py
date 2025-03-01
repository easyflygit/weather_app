from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/stats/', views.SearchHistoryStats.as_view(), name='search-history-stats'),
    path('api/weather/', views.WeatherView.as_view(), name='weather'),
    path('city-autocomplete/', views.city_autocomplete, name='city_autocomplete'),
    path('signup/', views.signup, name='signup'),
]