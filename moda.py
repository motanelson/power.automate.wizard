print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(a))
    return l

def moda(l:list):
    a:int=0
    count=0
    total=0
    value=0
    back=0
    lll=[]
    mm=0
    mn=0
    ll=copy.copy(l)
    ll.sort()
    for aa in ll:
        if count==0:
            mm=1
            back=copy.copy(aa)
            total=1
            value=copy.copy(aa)
        else:
            if back==aa:
                mm=mm+1
                if mm>total:
                    total=copy.copy(mm)
                    value=copy.copy(aa)
                
            else:
               back=copy.copy(aa)
               mm=1
        count=count+1
    return value


l=getlist(20)
l.append(5)
l.append(8)
l.append(8)
print(l)
print(moda(l))