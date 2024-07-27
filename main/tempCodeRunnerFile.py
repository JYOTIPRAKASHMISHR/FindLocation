import folium
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Replace with an actual phone number
phone_number_str = "+918260769942"

parsed_number = phonenumbers.parse(phone_number_str, None)
location = geocoder.description_for_number(parsed_number, "en")
carrier_info = carrier.name_for_number(parsed_number, "en")

print(f"Phone number: {phone_number_str}")
print(f"Location: {location}")
print(f"Carrier: {carrier_info}")

# Initialize OpenCageGeocode with your actual API key
key = "da0fbe6d86ba4bb5890c6840666735d4"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save('mylocation.html')
