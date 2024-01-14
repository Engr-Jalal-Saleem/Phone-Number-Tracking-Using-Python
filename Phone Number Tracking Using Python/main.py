import phonenumbers
import opencage
from myphone import number
from phonenumbers import geocoder
import folium
pepnumeber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumeber, "en")
print(location)
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
from opencage.geocoder import OpenCageGeocode
key = "a13f855bd74f48419a549167791f630ca13f855bd74f48419a549167791f630c"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
mymap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to((mymap))
mymap.save("mylocation.html")