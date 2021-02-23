from itertools import compress
def duplicate_sandwich(arr):
    arr1=set(arr)
    l=[]
    d=[]
    for i in arr:
        if i not in l:
            l.append(i)
        else:
            d.append(i)
    return [arr.index(d[0]) for x in arr if x==d[0]]
print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))