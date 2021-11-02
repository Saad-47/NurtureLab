from django.shortcuts import render
from rest_framework import viewsets
from .models import Advisor
from .serializers import AdvisorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Add Advisor':'/Admin/advisor',
		'Register User':'/User/register',
		'Login User':'/User/login/',
		'Refresh Token':'token/refresh/',
		'List of Advisors':'User/<str:user_id>/Advisor/List',
		'Advisor Booking':'User/<str:user_id>/Advisor/<str:advisor_id>/',
		'Booked Advisor':'User/<str:user_id>/Advisor/booking',
		}

	return Response(api_urls)

class AdvisorView(viewsets.ModelViewSet):
	serializer_class = AdvisorSerializer
	queryset = Advisor.objects.all()
    

