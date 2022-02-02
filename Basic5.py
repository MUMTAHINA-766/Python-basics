#leap year

"""
l_year = int(input())

if l_year%400 ==0:
    print('leap year')
elif l_year%100 == 0:
    print("leap year")
elif l_year%4 == 0:
    print("leap year")
else:
    print("not leap year")

"""
"""
#pattern-1 print

row = int(input())

count = 0
for i in range(0,row):
     for j in range(0,row-i-1):
         print(end=" ")
     
     count=count+1
     for k in range(0,i+count):
         print("*",end= "")

     print(" ")

"""

#pattern-2 print

"""
row = int(input())

for i in range(0,row):
     for j in range(0,row-i-1):
         print(end=" ")

     for k in range(0,i+1):
         print("*",end="")
     print(" ")
"""

#pattern-3 print
"""
row = int(input())

for i in range(0,row):
     for j in range(0,row-i-1):
         print(end=" ")

     for k in range(0,i+1):
         print("*",end=" ")
     print(" ")
"""

#pattern-4 print

"""
row = int(input())

for i in range(row):
     for j in range(i,row):
         print(end="*")
     print(" ")
"""
#pattern-5 print

"""
row = int(input())

for i in range(row):
    for j in range(i+1):
         print("#",end=" ")

    print(" ")
"""

#pattern-6 print
#my first successful pattern print :p

"""
row = int(input())

for i in range(row):
    for j in range(i,row):
        print(end=" ")
    for j in range((2*i)+1):
        print("*",end="")
    print(" ")
"""
#pattern-7 print diamond


row = int(input())

for i in range(row):
     for j in range(i,row):
        print(end=" ")
     for j in range(i+1):
         print("*",end=" ")

     print(" ")

for i in range(1,row):
     for j in range(i+1):
        print(end=" ")
     for j in range(i,row):
         print("*",end=" ")

     print(" ")

#pattern-7 print diamond 2.2.22

"""

row = 10
for i in range(row-1):
     for j in range(i,row):
        print(end=" ")
     for j in range(i+1):
         print("*",end=" ")

     print(" ")
print(" <<<<A N A N N A>>>>")
for i in range(1,row-6):
     for j in range(i+1):
        print(end=" ")
     for j in range(i,row):
         print("*",end=" ")
     print(" ")
print("     02 .02 . 22",end=" ")
print(" ")
for i in range(5,row):
     for j in range(i+1):
        print(end=" ")
     for j in range(i,row):
         print("*",end=" ")
     print(" ")
"""

