from collections import namedtuple
import json

Car=namedtuple('Car','color mileage'.split())
my_car=Car('red','38.90')
print(my_car.color)
print(Car)
print(my_car._asdict())
print(json.dumps(my_car._asdict()))
print(my_car._make(['yellow',78.00]))