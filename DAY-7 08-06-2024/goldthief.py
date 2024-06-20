#ip:13,9,4,10,5,7
#op:30

def gfun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+gfun(l[2:])
    print(le,l)
    ri=l[1]+gfun(l[3:])
    print(ri,l)
    return max(le,ri)

l=list(map(int,input().split()))
print(gfun(l))

    
    