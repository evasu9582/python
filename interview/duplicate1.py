def duplicate1(lst):
    seen = {}
    dupes = []

    for x in lst:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
                seen[x] += 1
    return seen,dupes
a=duplicate1([1,2,3,4,2,3,1,5,6])
print(a)