'''def fac(x):
    if(x==1):
        return 1
    return x * fac(x-1)#return fac(x-1) o/p 1 it will come check by tracing it
n=int(input())
print(fac(n))'''

'''ip:10
   op:sum of even numbers using recursion'''

def sum(n):
    if(n==0):
        return 0
    return n+sum(n-2)

n=int(input())
if(n%2==0):
    print(sum(n))
else:
    print(sum1(n-1))