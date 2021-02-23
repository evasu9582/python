import re 
regex=r"[a-zA-Z]+\d{1,2}"
data="June21,Jan19,Nov16,July21,Dec31"
match=re.findall(regex,data)
print(match)
# for m in match:
#     print(m)