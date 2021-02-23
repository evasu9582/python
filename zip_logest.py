from itertools import zip_longest

for i in zip_longest('hel','12345',fillvalue='#'):
    print(i)