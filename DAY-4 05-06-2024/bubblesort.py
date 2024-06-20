class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="-->")
            t=t.nxt
        print()
        
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
     
        
    def bubblesort(self):
        T=self.head
        p=None
        while(T.nxt!=None):
            f=0
            t=self.head
            while(t.nxt!=p):
                if (t.data)>(t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
            if f==0:
                break
            p=t
            T=T.nxt
                
l1=sll()        
l2=sll()

l1.head =node(6)
l1.addback(7)
l1.addback(4)
l1.addback(9)
l1.addback(4)
l1.addback(2)
l1.addback(0)
l1.addback(1)


l1.display()

l1.bubblesort()
l1.display()

                   
                   

