import operator
from itertools import accumulate
for i in accumulate([1,2,3,4,5],operator.mul):
    print(i)

for j in accumulate([2,3,4,5,6],operator.sub):
    print(j)


for k in accumulate([4,5,3,4,2,1,6,7],operator.add):
    print(k)