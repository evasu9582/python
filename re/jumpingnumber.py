def jumppingnumber(number):

    # return 'okk' if max(str(number)[-2:])-min(str(number)[-2:])<=1 or len(str(number))<=1 else 'Not'
    l_s=list(map(int,list(str(number))))
    l_st2=l_s[-2:]
    print(l_st2)
    f_st3=max(l_st2)-min(l_st2)
    print(f_st3)
    return 'Okk' if  f_st3!=0 or len(str(number))>=1  else 'Not'

print(jumppingnumber(999))