import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(
        serializer.data,
        ensure_ascii=False
    ).encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    data = json.loads(json.decode("utf-8"))
    serializer = CarSerializer(data=data)

    if serializer.is_valid():
        return serializer.create(serializer.validated_data)
    else:
        raise ValueError("Invalid car data: " + str(serializer.errors))
