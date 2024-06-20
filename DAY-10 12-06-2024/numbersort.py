'''
ip:[4,9,8,2,14,3,5,6]

op:4 8 9 2 14 3 5 6
'''



a=list(map(int,input().split()))
'''for i in range(len(l)-2):
    a=l[i]
    b=l[i+1]
    c=l[i+2]
    if a<b and a<c:
            l[i]=a
            if b<c:
                l[i+1]=b
                l[i+2]=c
            else:
                l[i+1]=c
                l[i+2]=b
    elif a<b and a>c:
        l[i]=c
        l[i+1]=a
        l[i+2]=b
    else:
        l[i]=b
        l[i+1]=a
        l[i+2]=c
    #print(l)
print(l)'''

'''for i in range(len(a)-2):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print(a)'''

for i in range(len(a)-2):
    s=a[i]+a[i+1]+a[i+2]
    a[i]=min(a[i],a[i+1],a[i+2])
    a[i+2]=max(a[i],a[i+1],a[i+2])
    a[i+1]=s-a[i]-a[i+2]
print(a)
