from rest_framework import serializers
from .models import Group, Events


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

