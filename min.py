print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(int(i-a)))
    return l

def mins(l:list):
    a:int=0
    count=0
    for aa in l:
        if count==0:
            a=aa
        else:
            if aa<a:
                a=aa
    return a


l=getlist(20)
print(l)
print(mins(l))