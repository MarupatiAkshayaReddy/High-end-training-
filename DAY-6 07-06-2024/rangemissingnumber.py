'''
ip:7-->range and lenght of list
   0 5 3 6 7 2 1
op:
  4
'''

n=int(input())
l=list(map(int,input().split()))
'''for i in range(n):
    if i not in (l): in and not in takes o(n) time complexity
        print(i)
        break
'''

s=sum(l)
print(s)
n=(n*(n+1))//2
print(n-s)
