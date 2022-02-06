#lists
#nested list
#negative index-serialization from the last eliment
#sublist and slicing

x = [20193290766,'Mumtahina',5.3]
y = [['Saidu',765,5.4],['Fazle',565,5.3]]
z = [1,2,3,4,5,6]

"""
print(x,y)
print(y[1][0])
print(x[-1])
print(x[0:2])
print(z[1:-2])
print(z[4:])
print(z[:])
"""
#add 2 list
#double,triple items
#delete items

xy = x + y
print(xy)
new_z = z*3
print(new_z)
del z[3]
print(z)
