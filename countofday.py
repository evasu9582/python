
def countofdays(trips):
    cou=[]
    for i in trips:
        a,b=i
        count=0
        for k in range(a,b+1):
            count+=1

        cou.append(count)
    return sum(cou)


a=countofdays([[10,15],[35,45]])
print(a)