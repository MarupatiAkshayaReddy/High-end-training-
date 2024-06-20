'''
ip:"the quick brown fox jumps over the lazy dog"
op:yes-->all 26 alphabets are present other wise no

ip:"qwweer yuiop asdfvgh jkl mnbvlkjcxz"
op:no

ip:the 4quick br$%^own foENDx j45umps o.ver the lazy dog
op:yes
'''

s=input()
'''s=set(s)
if len(s)==27:
    print("yes")
else:
    print("no")'''
'''
s=set(s)
c=0
for i in s:
    if i.islower():
        c=c+1
if c==26:
    print("yes")
else:
    print("no")'''

'''c=0
b="abcdefghijklmnopqrstuvwxyz"--->it takes extra space
for i in b::
    if(i not in s):
        print("no")
        break
else:
    print("yes")'''

'''for i in range(97,123):
    if(chr(i) not in a):
        print("no")
        break
else:
    print("yes")'''


d={}#instead of dictionary we can take empty set d=set()---we can take list too d=[0]*26
for i in s:
    if(i.islower()):
        d[i]=1#d.add(i) if set is took--- d[ord(i)-97]=1--if list is took


    
'''d=[0]*26
for i in s:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))'''#--->all operator returns True if all are non-zero values-->it returns false if any one value is zero

