from ketting import node
class queue:
    def __init__(self):
        self.backptr=None
        self.size=0

    def insert(self,naam):
        if self.size==0:
            self.backptr=node(naam)
            self.backptr.next=self.backptr
            self.size+=1
            return True
        else:
            old=self.backptr
            self.backptr=node(naam,self.backptr.next)
            old.next=self.backptr
            self.size+=1
            return True
    def isempty(self):
        if self.size==0:
            return True
        else:
            return False
    def getlength(self):
        return self.size

    def delete(self):
        if self.isempty()==False:
            self.backptr.next=self.backptr.next.next
            return True
        else:
            return False

    def gettop(self):
        if self.isempty()==False:
            return self.backptr.next
        else:
            return False

    def traverse(self):
        if self.isempty()==False:
            counter=0
            a=self.backptr.next
            while counter<self.size:
                print(a.item)
                a=a.next
                counter+=1
a=queue()
a.insert("hey")
a.insert("hello")
a.insert("howareyou")
a.traverse()
b=[]#test purpose