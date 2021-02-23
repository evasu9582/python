def last(*a):
    return a[0][len(a[0])-1] if type(a[0])==list or type(a[0])==str else a[len(a[0])-1]

print(last([1,2,3,4]))