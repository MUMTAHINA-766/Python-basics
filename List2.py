#list methods

places = ['Bang','Nep','Ind','Pak','uk','rs']

print(places.index('Pak'))

print(places.append('China'))
print(places)

places.insert(5,'USA')
print(places)

places.remove('Ind')
print(places)

places.sort()
print(places)
places.sort(key=str.lower)
print(places)
places.sort(key=str.lower, reverse=True)
print(places)
