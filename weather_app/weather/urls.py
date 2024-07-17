from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/stats/', views.SearchHistoryStats.as_view(), name='search-history-stats'),
]