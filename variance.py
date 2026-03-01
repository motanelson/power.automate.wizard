print("\033c\033[40;37m\n")
import copy
import math
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(int(a)))
    return l
def sums(l:list):
    a:int=0
    count=0
    total=0
    for aa in l:
        total=total+aa
    return total
def means(l:list):
    a:list=[]
    total=0
    count=0
    for aa in l:
        total=total+aa
        count=count+1
    total=total/count
    return total

def variance(l:list):
    meanss=means(l)
    a:list=[]
    total=0
    count=0
    for n in l:
       
        b=abs(n-meanss)
        d=b*b
        a.append(copy.copy(d))
    total=means(a)
    return total


l=getlist(20)
print(l)
print(variance(l))