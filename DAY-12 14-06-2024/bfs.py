def fun(d,x):
    v=[]
    q=[x]
    while(q):
        for i in d[q[0]]:
            if i not in v and i not in q:
                q.append(i)
        v.append(q.pop(0))
        #print(v[-1])--->we can get like this too it will print last nodes of v[] list
    return v
    
    
d={1:[2,5],2:[1,3,4],3:[2,7,9],4:[2,5,8],5:[1,4,6,11],6:[5,8],7:[3,8],8:[4,6,7],9:[3,10,12],11:[5],10:[9],12:[9]}
print(fun(d,next(iter(d))))#print(fun(d,1)) next(iter(d)) will give you the first key of the dictioanry
