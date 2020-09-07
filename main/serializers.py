from rest_framework import serializers
from .models import Specialty, Position, TypeRequest, MachineStatus


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ("id", "specialty")


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ("id", "position")


class TypeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRequest
        fields = ("id", "position")
