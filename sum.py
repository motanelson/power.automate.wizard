print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(a))
    return l

def sums(l:list):
    a:int=0
    count=0
    total=0
    for aa in l:
        total=total+aa
    return total


l=getlist(20)
print(l)
print(sums(l))