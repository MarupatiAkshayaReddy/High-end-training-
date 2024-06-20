'''
ip:
   "hello:5438,car:214,book:8799,apple:2187"
op:
oaxp
'''
a=input()
a=a.split(",")
b=[]
s=''
#print(str(a))
for i in range(len(a)):
    k=a[i]
    l=k.split(":")
    b.append(l)
print(b)

for i in range(len(b)):
    k=len(b[i][0])
    k1=list(b[i][1])
    d=len(k1)
    flag=0
    
    while(d!=0):
        if str(k) in k1:
           #print(k)
           a=b[i][0]
           s=s+a[k-1]
           flag=1
           break
        else:
            k=k-1
            if str(k) in k1:
                #print(k)
                a=b[i][0]
                s=s+a[k-1]
                flag=1
                break
        d=d-1
    if flag==0:
        s=s+'x'
        
            
print(s)
          
    
    
