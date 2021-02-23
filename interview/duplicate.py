
def duplicate(lst):
    ls=list(set(lst))
    return len(lst)-len(ls)
lst=[1,2,3,1,2,4,5,3,4,6,7,9,10]
print(duplicate(lst))