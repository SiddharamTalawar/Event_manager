from django.shortcuts import render
from rest_framework import viewsets
from .models import event
from .serializers import eventSerializer


class eventView(viewsets.ModelViewSet):
    queryset = event.objects.all()
    serializer_class = eventSerializer
  

