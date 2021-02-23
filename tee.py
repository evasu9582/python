from itertools import tee

for  i in tee([1,2,3,4,5,6,7],2):
    for j in i:
        print(j)

    print()