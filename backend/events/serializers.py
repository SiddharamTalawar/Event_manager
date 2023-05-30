from rest_framework import serializers
from .models import event

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ("event_name","discription","Agenda","tags","time","location","image","is_liked")