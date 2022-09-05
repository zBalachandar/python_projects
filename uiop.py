import phonenumbers
from phno import coder

from phonenumbers import geocoder
solve = phonenumbers.parse(coder, "CH")
print(geocoder.description_for_number(solve ,"en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(coder, "RO")
print(carrier.name_for_number(solve,"en"))