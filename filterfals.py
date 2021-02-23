from itertools import filterfalse

for i in filterfalse(lambda x:x%2,[1,2,7,9,5,3,2,9]):
    print(i)