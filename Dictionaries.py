# difference between list and dictionaries:

#list: index matters
from copy import copy


a = [1,2,3,4,5]
b = [5,4,3,2,1]
print(a == b)

#dictionaries : key matters not index

p = {'Country':'Bangladesh','Name':'Mumtahina'}
q = {'Name':'Mumtahina','Country':'Bangladesh'}
print(p == q)
r = {'Id':'20193290766'}
 
new_dic = p.copy()
new_dic.update(r)
print(new_dic)