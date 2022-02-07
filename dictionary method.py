p = {'Country':'Bangladesh','Name':'Mumtahina','ID':'20193290766'}

# printing values
for i in p.values():
    print(i)

# printing keys
for i in p.keys():
    print(i)

#printing key and value
for i in p.items():
    print(i)

# dictionary items making in list
x = list(p.keys())
y = list(p.values())
print(x,' \n',y)

# A handy trick to specify key and value
for k,v in p.items():
    print('Key: '+k+' value: '+v)

#check keys
print('Name' in p,'Name')
print('roll' in p,'roll')

#check values
print('Mumtahina' in p.values(),'Mumtahina')
print('Saidu' in p.values(),'Saidu')

#get method,if true then print the value,if not then print default value
print(str(p.get('Country','Default')))
print(str(p.get('City','Default')))

#setdefault(key,value)
print(p.setdefault('Country','notFound'))
print(p.setdefault('City','Rajshahi')) #if key not found then set a new key and print the value
print(p)