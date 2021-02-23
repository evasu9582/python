# def armstrong(num):
#     order=len(str(num))
#     sum=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum+=digit**order
#         temp//=10
#     if num==sum:
#         print(sum,'is armstrong ')

#     else:
#         print('is not armstrong')

# if __name__=='__main__':

#     a=armstrong(int(input('enter number :')))
#     print(a)

def arm1(num):
    order=len(str((num)))
    return sum([int(i)**order for i in str(num)])

if __name__=='__main__':
    a=arm1(int(input('enter number :')))
    print(arm1(1634))