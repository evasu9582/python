
def vaasu(cons_sum):
    b=int(input())
    a=cons_sum(b)
    if b==a:
        print('ok')
    else:
        print('not ok')
    
    
@vaasu
def cons_sum(num):
    lst=[i for i in range(0,num)]
    def con(lst):
        n=0
        for j in lst:
            n+=j
            if num==n:
                break
        print(n)
    return con(lst)






# if __name__=='__main__':
#     print(cons_sum(10))
