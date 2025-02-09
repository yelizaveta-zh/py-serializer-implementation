from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers
from car.models import Car


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000)
        ]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        required=False
    )

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data: dict) -> Car:
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
