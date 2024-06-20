n=int(input())
k=int(input())
c=1
if k==1:
    print(n)
else:
    i=n//2
    while i>0:
        if n%i==0:
            c=c+1
            if k==c:
                print(i)
                break
        i=i-1