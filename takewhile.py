from itertools import  takewhile

for i in takewhile(lambda x:x<9,[1,2,7,9,5,3,2,9]):
    print(i)