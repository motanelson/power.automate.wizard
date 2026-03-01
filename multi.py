print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(a))
    return l

def multi(l:list,n:int):
    a:int=0
    ll:list=[]
    count=len(l)
    for aa in range(count):
        
        a=l[aa]*n
        ll.append(copy.copy(a))
    return ll


l=getlist(20)
print(l)
print(multi(l,2))