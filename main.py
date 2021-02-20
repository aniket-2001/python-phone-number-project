import phonenumbers
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")

#IN BELOW LINE YOU WILL COUNTRY LOCATION OF PHONENUMBER
print("1.This is your country:\n")
print(geocoder.description_for_number(ch_number,"en"))
print("--------------------------------------------------------------------------------------------")

#NOW LETS ALSO FIND THE SERVICE PROVIDER OF THIS PHONE NUMBER

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("2.This is your Service Provider:\n")
print(carrier.name_for_number(service_number, "en"))
print("----------------------------------------------------------------------------------------------")


#LETS FIND THE TIMEZONE NOW
from phonenumbers import timezone
gb_number = phonenumbers.parse(number, "GB")

print("3.This is your Timezone:\n")
print(timezone.time_zones_for_number(gb_number))
print("----------------------------------------------------------------------------------------------")

