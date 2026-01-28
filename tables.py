import random
def returning():
    a=random.random()*15
    a=int(a)
    a=chr(32+a)
    
    return a
print( "\n\033c\033[40;37m\ngive the x value of the table ? ")
x=79
y=200
c=0
a="bitmap.dat"
x=int(input())
print( "\n\033[40;37m\ngive the y value of the table ? ")
y=int(input())
print( "\n\033[40;37m\ngive the color 0 to 15 ? ")
c=int(input())+32
f1=open(a,"w")
for yy in range(y):
    
    for xx in range(x):
        f1.write(chr(c))
    f1.write(chr(10))
f1.close()
