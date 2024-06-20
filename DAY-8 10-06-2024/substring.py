'''
ip:
  "abfgresagtyuiofde"
op:
  12
  print lenght of longest substring without repeating characters
  
'''
a=input()
d={}
s=""
i,m=0,0

while(i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)

    
