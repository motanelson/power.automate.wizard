print("\033c\033[40;37m\n")
import random
import copy


def ranges(froms:int,intos:int,steps:int):
    r=[]
    rands=intos-froms
    counts=0;
    while(1):
        if counts>=rands:
             break
        rr=counts+froms
        r.append(copy.copy(rr))
        counts=counts+steps
        
        
    return r

a=ranges(-10,10,2)
print(a)

