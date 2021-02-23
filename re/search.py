import re
s=input("Enter a pattern a check :")
m=re.search(s,'abaaabccdhhv')
if m!=None:
    print("Full string matched")

else:
    print("Match is not available")