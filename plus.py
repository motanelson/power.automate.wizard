print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(a))
    return l

def plus(l:list,ll:list):
    a:int=0
    total:int=0
    count=len(l)
    count1=len(ll)
    lll=[]
    if count1!=count:
        return lll
    for aa in range(count):
        total=l[aa]+ll[a]
        lll.append(copy.copy(total))
    return lll


l=getlist(20)
ll=[1]*len(l)
print(l)
print(ll)
print(plus(l,ll))