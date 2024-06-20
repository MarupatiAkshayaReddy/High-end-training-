'''
ip:
   [3 5 9 6 8 10]
op: 4 1
ip:[3 4 5 10 4 3]
op:4 3

mrng how many buildings sun will fall in evng how many buildings sun will fall

'''
l=list(map(int,input().split()))
mc,ec=1,1
maxm=l[0]
maxe=l[-1]
#morning
for i in range(1,len(l)):
    if l[i]>maxm:
        mc+=1
        maxm=l[i]
#evng
for i in range(len(l)-1,-1,-1):
    if l[i]>maxe:
        ec+=1
        maxe=l[i]
print(mc,ec)
