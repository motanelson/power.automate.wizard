print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(int(a)))
    return l

def finds(l:list,n:int):
    a:list=[]
    count=0
    for aa in l:
        if aa==n:
            a.append(copy.copy(int(aa)))
    return a


l=getlist(20)
print(l)
print(finds(l,5))