"""
a = 100
b = 200
c = 300

def processor(arg):
    print('processing stuffs!')
    global a
    global b
    global c
    c += arg + b + a
    print(c)
processor(10)
"""

def mod_div_calculation(num1, num2, calc_type):
     if calc_type == '%':
         print(num1 % num2)
     elif calc_type == '/':
         print(num1 / num2)
mod_div_calculation(4,2,"/")