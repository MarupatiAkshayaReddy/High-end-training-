'''
ip:121          ip:122     ip:1234        ip:24       ip:1112    ip:7654    ip:56472    ip:76583   ip:12412
op:121          op:131     op:1331        op:33       op:1221    op:7667    op:56565    op:76667   op:12421


if not a palindrome you have to print next possible palindrome
'''

n=input()
if len(n)%2==0:
    t=n[0:len(n)//2]
    k=t+t[::-1]
    if k<n:
        t=t[:-1]+str(int(t[::-2])+1)
        k=t+t[::-1]
    print(k)
else:
    t=n[0:(len(n)//2)]
    k=t+(n[len(n)//2])+t[::-1]
    if k<n:
        a=str(int((n[len(n)//2]))+1)
        k=t+a+t[::-1]
    print(k)
    
    
    
    

