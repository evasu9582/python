import re
with open('emp.txt','a') as p:
    data=p.write("1001,scott,2000.00,miller,5000.00,1001,3000.00,1003,blake")
    print(data)
    regex=r"[a-zA-Z]+\d{0}"

with open('emp.txt','r') as r:

    data1=r.readline()
    matches=re.findall(regex,data1)
    print(set(matches))
