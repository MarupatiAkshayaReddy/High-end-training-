'''
ip:"MMFFMFFMFMFMFMFFMMFF"
COUNT OF FEMALE>COUNT OF MALE ->OP:F
COUNT OF MALE>COUNT OF FEMALE ->OP:M
COUNT OF FEMALE=COUNT OF MALE ->OP:0'''

s=input()
if (s.count('M') or s.count('m')) == (s.count('F') or s.count('f')):
    print("0")
elif (s.count('M') or s.count('m')) > (s.count('F') or s.count('f')):
    print("M")
else:
    print("F")
    
    
'''
c=0
for i in s:
if(i=='M'):
c=c+1
else:
c=c-1

if c>0:p("M")
elif c==0:p("0")
else c<0:p("F")'''