import os

f = open('Test.txt', 'r')
f.write('Hello world')
print(f.read())
f.close()
list = f.readlines()