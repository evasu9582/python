def pawn(N,P):
    cn=[]
    if N:
        for i in range(N,P+1):
            cn.append(i)
    else:
        for j in range(N,P):
            cn.append(j)
    decision=max(cn)
    return ('Block',decision*2) if decision%2==0 else ('White',decision*2)

print(pawn(0,8))