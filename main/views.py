from django.shortcuts import render
import json
import urllib.request
import math
from urllib.error import HTTPError
# Create your views here.
def index(request):
    key = '6f12a083411ca9a9dd663873c406fabf'
    if request.method == 'POST': 
        city = request.POST['city'] 
        try :
            source = urllib.request.urlopen( 
                'http://api.openweathermap.org/data/2.5/weather?q=' 
                        + city + '&appid='+key).read() 
            list_of_data = json.loads(source)     
            
            data = { 
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": 'Latitude : '+str(list_of_data['coord']['lat']) + ' '
                            +'Longitude : '+ str(list_of_data['coord']['lon']), 
                "temp": str(math.trunc(list_of_data['main']['temp']-273.15)) + ' C', 
                # "pressure": str(list_of_data['main']['pressure']), 
                "humidity": str(list_of_data['main']['humidity']), 
                "name" :str(list_of_data['name'])
            } 
        except HTTPError as err:
            print(err.code)
            if err.code == 404 :
                data = {
                        "error" : "Couldnt find this city"
                    }
                print(err)

    else :
        data = {}
    return render(request,'main/index.html',data)