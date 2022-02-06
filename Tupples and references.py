# tuples are immutable version of list(non changable)
# tuples are faster than list
"""
x = (1,2,3,4,5,6)

print(x)
print(type(x))
print(x[5])
print(x[3:6])

y = list(x)
print(y)
print(type(y))
"""
# reference
import copy as cp 

a = [1,2,3,4]
b = a #copied just the reference not the elements

c = a.copy() #copied the elements in c

b.append('ok') #changed the reference of a but c unchanged

print(b)
print(c)



