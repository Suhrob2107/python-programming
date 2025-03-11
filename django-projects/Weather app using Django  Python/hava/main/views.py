from django.shortcuts import render
import json  # JSON verilerini işlemek için
import urllib.request  # API'ye istek atmak için


def index(request):
    data = {}  # Varsayılan boş veri
    if request.method == 'POST':
        city = request.POST['city']

        # OpenWeatherMap API URL'si (kendi API anahtarını eklemelisin)
        api_key = "bd5e378503939ddaee76f12ad7a97608"  # Kendi API anahtarını buraya yaz!
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            source = urllib.request.urlopen(url).read()
            list_of_data = json.loads(source)

            # API’den gelen veriyi uygun şekilde işleyip frontend’e göndermek
            data = {
                "city": city,
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                "temp": str(list_of_data['main']['temp']) + ' K',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
        except:
            data = {"error": "Şehir bulunamadı veya API hatası oluştu!"}

    return render(request, "main/index.html", {"data": data})
