#quizes

import copy as cp
s = [10, 20]
s.append(60)
n = cp.copy(s)
n.append(60)
x = cp.copy(n)
x.append(60)
print(s,n,x, sep = '#')

"""
aList = [5, 10, 15, 25]
print(aList[::-2])
"""