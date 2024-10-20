class Deque:
    def __init__(self):
        self.li=[]
    def Append(self,data):
        self.li+=[None]
        self.li[-1]=data
    def Appendleft(self,data):
        self.li=[None]+self.li
        self.li[0]=data
    def is_empty(self):
        if self.li==[]:
            return True
        return False
    def Pop(self):
        if self.is_empty():
            print("is empty")
            return
        x=self.li[-1]
        self.li[-1]=None
        del(self.li[-1])
        print(x)
    def Popleft(self):
        if self.is_empty():
            print("is empty")
            return
        x=self.li[0]
        self.li[0]=None
        del(self.li[0])
        print(x)
    def Peek(self):
        if self.is_empty():
            print("is empty")
            return
        print(self.li[-1])
    def Peekleft(self):
        if self.is_empty():
            print("is empty")
            return
        print(self.li[0])
    def Size(self):
        if self.is_empty():
            print("is empty")
            return
        print(len(self.li))

obj=Deque()
n=int(input("Enter no of elements : "))
for i in range(0,n):
    lst=input("Eneter operation and value with spsaces : ").split()
    if (lst[0]=="append"):
        obj.Append(lst[1])
    elif(lst[0]=="appendleft"):
        obj.Appendleft(lst[1])
    elif(lst[0]=="peek"):
        obj.Peek()
    elif(lst[0]=="peekleft"):
        obj.Peekleft()
    elif(lst[0]=="pop"):
        obj.Pop()
    elif(lst[0]=="popleft"):
        obj.Popleft()
    elif(lst[0]=="size"):
        obj.Size()
    elif(lst[0]=="is_empty"):
        print(self.is_empty)
