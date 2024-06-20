'''def pairs(l,i):
    
    if len(l)-i==2:
        return 
    t=l[i]
    for k in range(i+1,len(l)):
        for j in range(k+1,len(l)):
            print(t,end="")
            print(l[k],end="")
            print(l[j],end=" ")
    print()
    return pairs(l,i+1)
              
    
l=list(map(int,input().split()))
pairs(l,0)'''


def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr,end=" ")
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        print()
        return
    fun([],0)
    
l=list(map(int,input().split()))
k=int(input())
combination(l,k)


            
