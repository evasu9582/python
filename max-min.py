def maxmin(seq):
    st=sorted(seq)[::-1]
    lst=[]
    while len(st):
        lst.append(st.pop(0))
        if len(st):
            lst.append(st.pop())

    return lst

if __name__=='__main__':
    seq=[15,10,7,11,2,13]
    print(maxmin(seq))
