'''
ip:abdbsdabca
op:bdb

print the longest palindromic substring(we will not skip the letters--all together)
op:if not available -1
  if available print it
  
subsequence--->jumping  the letters
'''

'''str=input()
res=[]
def ispal_rev(left,right):
    n=len(str)
    while left>=0 and right<n and str[left]==str[right]:
        left-=1
        right+=1
    return str[left+1:right]
    


for i in range(len(str)):
    
    pal1=ispal_rev(i,i)
    
    if len(pal1)>1:
        res.append(pal1)
        print(res)
    pal2=ispal_rev(i,i+1)
    if len(pal2)>1:
        res.append(pal2)
        print(res)
    print(res)
    

print(res)
print(max(res))
        '''


# abbbcbbba
# abbbabcbabbba 

