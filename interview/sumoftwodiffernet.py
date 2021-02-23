def or_arrays(arr1, arr2):
    arr=set(arr1+arr2)
    if len(arr)==len(arr1):
        return arr1
    else:
        return [i+j for i,j in zip(arr1+arr2)]

print(or_arrays([1,2,3],[1,2,3]))