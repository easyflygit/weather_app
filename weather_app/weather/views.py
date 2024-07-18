from django.shortcuts import render
from .forms import CityForm
from .utils import get_weather
from .models import SearchHistory
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchHistorySerializer


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather = get_weather(city)
            if weather:
                request.session['last_city'] = city
                if request.user.is_authenticated:
                    search_history = SearchHistory.objects.filter(user=request.user, city=city).first()
                    if search_history:
                        search_history.search_count += 1
                        search_history.save()
                    else:
                        SearchHistory.objects.create(user=request.user, city=city, search_count=1)
                return render(request, 'weather/index.html', {'form': form, 'weather': weather})
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {'form': form})


def search_stats(request):
    stats = SearchHistory.objects.all().values('city', 'search_count')
    return JsonResponse(list(stats), safe=False)


class SearchHistoryStats(APIView):
    def get(self, request, format=None):
        search_stats = SearchHistory.objects.all()
        serializer = SearchHistorySerializer(search_stats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WeatherView(APIView):
    def get(self, request, format=None):
        city = request.GET.get('city', None)

        if not city:
            return Response({'error': 'City parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_authenticated:
            search_history = SearchHistory.objects.filter(user=request.user, city=city).first()
            if search_history:
                search_history.search_count += 1
                search_history.save()
            else:
                SearchHistory.objects.create(user=request.user, city=city, search_count=1)

        weather = get_weather(city)
        if weather:
            return Response({'city': city, 'weather': weather}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to fetch weather data'}, status=status.HTTP_400_BAD_REQUEST)