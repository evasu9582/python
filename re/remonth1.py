import re
regex=r"[a-zA-Z]+\d{0}"
data="June12,July15,Aug15,Nov1,Dec31"
matches=re.findall(regex,data)
print(matches)