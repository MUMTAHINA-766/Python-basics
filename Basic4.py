#loops

#infinite-1

"""
while True:
    print('Please Enter your correct name!')
    name = input()
    if name == 'Mumtahina':
        break
print('Correct name')
"""

#infinite-2
from os import O_TEMPORARY
"""

while True:
    print('Who are you?')
    name = input()
    if name!= 'Omy':
        continue
    print('Please Enter your PW '+ name +'\n Password')
    password = input()
    if password == 'Peace':
        break
print('pw correct')

"""

#series loop-1

"""
sum = 0
for i in range(1, 5):
    sum = sum+i

print(sum)

"""
#series loop-2

"""
sum = 0
for i in range(1, 5):
    sum = sum +(i*i)
    print(sum)

"""
#series loop-3(2+4+6..+10)

"""
even_sum = 0
for i in range(1, 10):
    even_sum = even_sum+2*i
    print(even_sum)

"""

#series loop-4 (1+3+5..)

"""
odd_sum = 0
for i in range(0,10):
    odd_sum = odd_sum+((2*i)+1)
    print(odd_sum)

"""
#series loop-3a(2+4+6..+10)
"""
sum = 0
for i in range(1,10,2):
    sum = sum+i
    print(sum)
"""

##series nested loop-3(1+(1+2)+(1+2+3)...)

sum=0
for i in range(1,5):
    for j in range(1,i+1):
        sum=sum+j
    print(sum)