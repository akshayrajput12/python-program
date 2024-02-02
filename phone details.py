import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter a number with +__: ")
phone = phonenumbers.parse(number)

time_zones = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
region = geocoder.description_for_number(phone, "en")

print("Time Zones:", time_zones)
print("Carrier:", car)
print("Region:", region)
