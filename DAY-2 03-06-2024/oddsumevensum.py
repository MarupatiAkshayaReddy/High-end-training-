'''using recursions print ->both list same lenghts
a=[3,8,5,4,3]
b=[5,0,9,3,2]

op:(a list even sum,b list odd sum)
   (12,17)'''



# ->both list same lenghts you can take i single variable instead of x,y
def sum(x,y,esum,osum):
    if (x==len(a) and y==len(b)):
        return esum,osum
    else:
        if a[x]%2==0:
            esum=esum+a[x]
            #print(esum)
        if b[y]%2!=0:
            osum=osum+b[y]
            #print(osum)
    return sum(x+1,y+1,esum,osum)
        
''''def sum(i,esum,osum):
    if (i==len(a)):
        return esum,osum
    
    if a[i]%2==0:
        esum=esum+a[x]
        #print(esum)
    if b[i]%2!=0:
        osum=osum+b[y]
        #print(osum)
    return sum(i+1,esum,osum)
    
    
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x,y=sum(0,0,0)
print(x,y)    '''            
    
    
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(sum(0,0,0,0))