def maxmin(lst):
    ls1=sorted(lst)[::-1]
    ls=[]
    for i in ls1:
        ls.append(i)
        ls.append(ls1.pop())

    return ls
print(maxmin([15,10,11,8,7,5]))