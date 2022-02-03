#Armstrong number
#abc=pow(a, n) + pow(b,n) + pow(c,n)
#abcd=pow(a, n) + pow(b,n) + pow(c,n) + pow(d,n)
#Armstrong number-for 3 digit
"""
print("Enter the number: ")

digit = int(input())
temp = digit
sum = 0
while digit != 0:
    digit_mod = digit % 10
    digit = digit//10
    sum = sum + digit_mod**3
if sum == temp:
    print("The number is armstrong.")
else:
    print("The number is not armstrong.")
"""
#Armstrong number-for any digits:
#371,351,

n = int(input("Enter the number:\n "))
sum = 0
order = len(str(n))
copy_n = n
while(n>0):
    digit = n % 10
    sum += digit ** order
    n = n//10

if(sum == copy_n):
    print(copy_n, " is an armstrong number")
else:
    print(copy_n ," is an armstrong number")

#quizes
"""
y = 10
a = 20
b = 51

if a > 19:
    if b < 0: 
        if y == 10:
            y = y + 111
    elif a > 5:
        y = y + 41
    else:
        y = y + 30
else:
    y = y + 22

print(y)
"""
"""
num = 0

for i in range(5):
    for j in range(0, -100, -1):
        num += 1
print(num)
"""
#error
"""
x = 0
while (x < 100):
    x+=2
if x % 33 == 0:
    print('This is an awkward loop!')
"""
"""
for i in range(1001, 2001, 202):
     for j in range(-15, -150, -2):
      for k in range(1, 10):
       print(i,j,k, end=',')
"""
