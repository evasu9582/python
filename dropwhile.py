from itertools import dropwhile
for i in dropwhile(lambda x:x<7,[1,2,7,9,5,3,2,9]):
    print(i)