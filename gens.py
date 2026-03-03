print("\033c\033[40;37m\n")
import random
import copy


def rnds(i:int,froms:int,intos:int):
    r=[]
    rands=intos-froms
    
    for n in range(i):
        rr=int(random.random()*rands)+froms
        r.append(copy.copy(rr))
    return r

a=rnds(100,-10,10)
print(a)

