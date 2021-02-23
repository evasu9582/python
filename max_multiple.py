def max_multiple(div,bound):
    s=[i for i in range(div,bound)]
    return max([j for j in s if j%div==0])
if __name__=='__main__':
    print(max_multiple(3,10))