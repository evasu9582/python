from itertools import groupby

for i,j in groupby('AAABBBCAAATTTVVUYV'):
    print(list(j))