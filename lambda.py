''''
synatx:
lambda argument : manipulate(argument)
'''

def add(a,b):
    s = a+b
    return s

addition = lambda x,y:x+y

#print(add(2,3))
#print(addition(2,3))

a = [(4,3), (1,5),(1,2,3,4), (123, 1), (1,)]
a.sort(key= lambda x:len(x))
print(a)