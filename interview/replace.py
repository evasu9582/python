def replace_all(obj, find, replace):
    if type(obj)==list:
        l_St=obj
        for i in obj:
            if i==find:
                l_St[l_St.index(i)]=replace
        return l_St

print(replace_all([1,2,2],1,2))