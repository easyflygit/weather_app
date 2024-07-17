from django.shortcuts import render
from .forms import CityForm
from .utils import get_weather
from .models import SearchHistory
from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather = get_weather(city)
            if weather:
                request.session['last_city'] = city
                search, created = SearchHistory.objects.get_or_create(city=city)
                search.search_count += 1
                search.save()
                return render(request, 'weather/index.html', {'form': form, 'weather': weather})
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {'form': form})


def search_stats(request):
    stats = SearchHistory.objects.all().values('city', 'search_count')
    return JsonResponse(list(stats), safe=False)