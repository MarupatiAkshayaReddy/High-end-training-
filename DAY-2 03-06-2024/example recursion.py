'''def fun(x):
    print(x)
    fun(x+1)
fun(1)'''

'''def fun(x):
    if(x==6):
        return 
    print(x)
    fun(x+1)
    print(x)
fun(1)
print("hi")'''


'''x=1 it is a loop it returns too hii line
while(1):
    if(x==6):
        break
    print(x)
    x=x+1
print("hi")'''


'''def fun(x):
    return x+10
print(fun(5)) '''
    
    
'''def fun(x):
    if(x==3):
        return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
print(fun(1))   '''

def fun(x,s):
    if(x==len(a)):
        return s
    s=s+a[x]
    return fun(x+1,s)#t=fun(x+1,s)
    #return t
a=[6,7,2,5]
print(fun(0,0))