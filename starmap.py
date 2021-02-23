from itertools import starmap
import operator
for i in starmap(operator.sub,[(2,1),(7,3),(15,10)]):
    print(i)