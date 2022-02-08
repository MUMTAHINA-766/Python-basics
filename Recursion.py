# factorial calculation in simple way and recursive way
#type 1

from ast import Num


def factorial(n):
    temp = 1
    for i in range(2,n+1):
        temp = temp*i

    return temp
num = input()
print(factorial(int(num)))

#type 2-recursive way

def factorial2(n):
  if n == 1:
      return 1
  return n*factorial2(n-1)

    
num = input()
print(factorial2(int(num)))