import re

"""
def outer(message):
    print('This is outer function')

    def inner():
        print('This is the inner function')
        print(message)

    return inner

f = outer("Hello Omy")
#print(f)
f()
"""

#decorator

def decorator(original_func):

    print("In the decorator function\n")

    def wrapper():
        print(f'wrapper executer before {original_func.__name__}()')

        if 10> 5:
            print('It is true')
        return original_func() 

    return wrapper


@decorator
def print_something():
    print('Print something is being ran!')
# #using decorator in one way without @decorator
# decorated_f = decorator(print_something)
# decorated_f()

print_something()

