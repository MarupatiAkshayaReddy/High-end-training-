import math

a=int(input())
b=int(input())

'''if math.gcd(a,b)==1:
    print("co-prime")
else:
    print("not co-prime")'''
        
for i in range(2,(min(a,b)//2)+1):
    if(a%i==0) and (b%i==0):
        print("not co-prime")
        break
else:
    print("co-prime")
    
