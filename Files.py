#'r'(read),'r+'(read+write),'w'(write),'w+'(write + read),'a'(append),'a+'(append+read)


f = open('p.txt','w+')

print('name= ',f.name)
print(f.closed)
print(f.mode)
f.write('this is last try')
f.close()

"""
f = open('p.txt','a')
f.write('please go on')
f.close
"""
"""
f = open('p.txt','r+')
info = f.read(20)
print(info)
"""

