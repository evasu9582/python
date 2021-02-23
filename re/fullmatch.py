import re
in_put=input('enter name :')
print(in_put)
regex=re.fullmatch(r'Harish',in_put)
if regex==None:
    print('string not matched')

else:
    print("full string matched")
