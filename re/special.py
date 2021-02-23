import re
def SpecialorNot(number):
    st=str(number)
    s_t=list(map(int,list(st)))
    special=[0,1,2,3,4,5]
    set_special=set(special)
    return "Special!!" if len(set(s_t+special))==len(set_special) else "NOT!!"

print(SpecialorNot(11350224))