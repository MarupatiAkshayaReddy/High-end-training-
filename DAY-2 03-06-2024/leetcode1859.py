s=input().split()
res=[0]*len(s)
for i in s:
    res[int(i[-1])-1]=i[:-1]
        
print(" ".join(res))