from django.shortcuts import render
from . import models
from .serializers import CarSerializer 
from rest_framework import viewsets      

class CarView(viewsets.ModelViewSet):  
	serializer_class = CarSerializer   
	queryset = models.Car.objects.all()
