#write a function to check if the number odd or even

"""
def check_even_odd(n):
    if n%2 == 0:
        print("even")
    else:
        print("odd")
check_even_odd(int(input()))
"""

#if the number prime or not


import math
def check_prime(n):
    count = 0
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            print("Not prime")
            break
        count = count+1
    if count+2 == math.floor(math.sqrt(n))+1:
        print("prime")

n = int(input())        
check_prime(n)

"""
#easy way 

num = int(input())

for i in range(2,num):
    if num%i == 0:
        print("not prime")
        break
else:
    print("prime")
"""




#highest common factor between two numbers(factor-if a is divided by b then b is a factor)
#write a small function to depict a rock-paper-scissors game.your function should take two inputs and should give us the winner based on a certain condition.

