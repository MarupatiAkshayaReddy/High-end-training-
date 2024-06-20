s=input()
l=[]
for i in s:
    if i!='*':
        l.append(i)
    if i=='*':
        l.pop()
    
print("".join(l))
        

        
        
        