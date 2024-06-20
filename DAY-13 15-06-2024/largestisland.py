'''
ip:
  5
  0 1 0 0 1         1-->land
  1 0 0 1 1         0-->water
  0 0 0 0 0
  1 0 0 0 0
  1 0 0 0 1
  
  op:5
'''



'''def fun(arr,n,r,c,co):
    if r<0 or c<0 or r>=n or c>=n or arr[r][c]!=1:
        return co
    if arr[i][j]==1:
        arr[r][c]=2
        co=co+1
    co=fun(arr,n,r-1,c,co)#top
    co=fun(arr,n,r,c-1,co)#left
    co=fun(arr,n,r+1,c,co)#bottom
    co=fun(arr,n,r,c+1,co)#right
    
   
    return co
    
    
        
arr=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n=len(arr)
arr=[]
for i in range(n):
    col=[]
    for j in range(n):
        val=int(input())
        col.append(val)
    arr.append(col)
print(arr)
r=int(input())
c=int(input())



ct=0
m=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            k=fun(arr,n,i,j,0)
            if(k>m):
                m=k
            ct=ct+1
print(ct,k)
print(arr)'''


def fun(i, j, c):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return c
    a[i][j] = 2
    c += 1
    c = fun(i, j-1, c)
    c = fun(i, j+1, c)
    c = fun(i-1, j, c)
    c = fun(i+1, j, c)
    return c

a = [[1, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1]]
n = 4
co = 0
m = 0
for i in range(4):
    for j in range(4):
        if a[i][j] == 1:
            k = fun(i, j, 0)
            if k>m:
                m=k
            co+=1
print(co, m)        







