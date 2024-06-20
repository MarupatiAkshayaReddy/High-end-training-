'''
ip:[4,8,2,4,4,8,4]
print a number from this list where the frequency of that number is more than the half of the length of list
list should be given in such a way that answer is always possible
op:4


ip:[2,1,2,2] op:2
io:[6,6,6,6,7] op:6
io:[4,9999,2,4,4,8,4] op:4
'''
l=list(map(int,input().split()))
n=len(l)//2
c=1
w=l[0]
'''c=[]
for i in range(len(l)):
    c.append(l.count(l[i]))
    if c[i]>n:
        print(l[i])
        break'''

for i in range(1,len(l)):
    if l[i]==w:
        c=c+1
    else:
        c=c-1
        if c==0:
            w=l[i]
            c=1
print(w)

'''for i in range(1,len(l)):
    if l[i]!=w:
        c=c-1
        if c==0:
            c=1
            w=l[i]
    else:
        #w=l[i]
        c=c+1
print(w)'''


    
    
    


    
    


