from collections import namedtuple

a=namedtuple('Car',['color','mileage'])
ak=a('red',89.00)
print(ak.color)
print(ak.mileage)
print(ak[0])
print(*ak)
print(ak)