"""
#1
s = 'terfinx'
s = ''.join(sorted(list(s)[3:7])+list(s)[0:3])
print(s)
#2
print('P"yt\'h"on')
#3
s1 = "Ronaldo is better than Messi"
print("Ronaldo" in s1)
print("Football" in s1)

#4
x = 50*2+(60-20)/4
print(x)

#5
python = ['cool']
x = python in python
print(x)

#6
l =[[]]
if l:
    print(True)
else:
    print(False)
"""
"""
#7
def ask_ok(promt, retries=4, reminder='Repeat!'):
    while True:
        ok = input(promt)
        if ok in ('y','ye','yes'):
            return True
        if ok in('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Howdy?',5)
"""

#8
words = ['ape','banana','cat','bird']
b_word = [w for w in words if w.startswith('b')]

print(len(b_word))