'''
ip:
  non-prime numbers in increasing order
  [4,8,14,22,36,68]
  4 8-->largest prime number is 7 13 19 
  print sum of all prime numbers'''


def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0
        
    

l=list(map(int,input().split()))
s=0
for i in range(len(l)-1):
    #print(lprime(l[i],l[i+1]))
    s=s+lprime(l[i],l[i+1])
print(s)

    

            
        