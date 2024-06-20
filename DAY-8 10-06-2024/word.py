'''
ip:
   4-->matrix
   t u e d
   f w o w
   r o e r
   d r u i
   
   string-->word
   
op:
  it is available yes or no
'''


def fun(arr,s,i,j,k,t):
    if i<0 or j<0 or i>=n or j>=n or arr[i][j]!=s[k]:
        return

    if arr[i][j]==s[k]:
        arr[i][j]=0
        t=fun(arr,s,i-1,j,k+1)#top
        t=fun(arr,s,i,j-1,k+1)#left
        t=fun(arr,s,i,j+1,k+1)#right
        t=fun(arr,s,i+1,j,k+1)#bottom
        return t

    
    
n=int(input())
arr=[]
for i in range(n):
    col=[]
    for j in range(n):
        val=(input())
        col.append(val)
    arr.append(col)
print(arr)
s=input()

fun(arr,s,0,0,1,0)

for i in range(n):
    for j in range(n):
        if(arr[i][j]==s[0]):
            c=fun(i,j,1,0)
            if c==1:
                print("yes")
                break
if c==0:
    print("no")
'''if str==s:
    print("yes")
else:
    print("no")
'''

