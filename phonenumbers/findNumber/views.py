import phonenumbers
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from phonenumbers import timezone, carrier, geocoder


def find_number(request):
    return render(request, 'findNumber.html')


class FindNumberDetails(APIView):
    def post(self, request, *args, **kwargs):
        print('Mobile Number', request.data)
        number = request.data.get('number')
        if not number:
            raise serializers.ValidationError("Mobile number is not provided.")

        try:
            phone = phonenumbers.parse(number)
        except Exception as e:
            raise serializers.ValidationError("Please provide a valid Mobile Number.")

        if not phonenumbers.is_valid_number(phone):
            raise serializers.ValidationError("Please provide a valid Mobile Number.")

        tz = timezone.time_zones_for_geographical_number(phone)
        service_provider = carrier.name_for_valid_number(phone, 'en')
        region = geocoder.description_for_valid_number(phone, 'en')

        return Response({
            'country_code': phone.country_code,
            'mobile_number': phone.national_number,
            'timezone': tz,
            'service_provider': service_provider,
            'country': region
        })


class FindNumbersInText(APIView):
    def post(self, request, *args, **kwargs):
        print('Mobile Number', request.data)
        mobile_numbers = []
        for match in phonenumbers.PhoneNumberMatcher(request.data.get('text'), ''):
            mobile_numbers.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))

        return Response({
            'mobile_numbers': mobile_numbers
        })
