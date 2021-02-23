import re
regex=re.compile(r"good")
data="Python good hello good Python"
matches=re.finditer(regex,data)
for i in  matches:
    print(i.start(),i.end())

matches1=re.match(r"hello","hello vaasu its good python hello")
print(matches1.start())