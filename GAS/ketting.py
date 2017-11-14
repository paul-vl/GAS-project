import copy
class node:
    def __init__(self,item=None,next=None,previous=None):
        self.item=item
        self.next=next
        self.previous=previous
class doubleketting:
    def __init__(self):
        self.head=node(None)
        self.head.next=self.head
        self.head.previous=self.head
        self.size=0
    def insert(self,item,position):
        counter=0
        a=self.head
        while counter<position:
            if counter==position-1 or counter==self.size-1:
                previous=a
            a=a.next
            counter+=1
        previous.next=node(item,a,previous)
        previous.next.next.previous=previous.next
        self.size+=1
        return True

    def isempty(self):
        if self.size==0:
            return 1
        else:
            return 0

    def getlength(self):
        return self.size

    def traverse(self):
        counter=1
        if self.isempty()!=1:
            a=self.head.next
            while counter<=self.size:
                print(a.item)
                a=a.next
                counter+=1
            return True
        else:
            print("this ketting is empty")
            return False

    def delete(self,position):
        counter=1
        if position>self.size or position<1:
            print("position out of range")
            return False
        else:
            a=self.head.next
            while counter<position:
                a=a.next
                counter += 1
            a.previous.next=a.next
            self.size-=1
            return True

    def retrieve(self,position):
        if position>self.size or position<1:
            print("position out of range")
            return False
        else:
            counter = 1
            a=self.head.next
            while counter<position:
                a=a.next
                counter+=1
            return a.item


ketting=doubleketting()
ketting.insert(5,1)
ketting.insert(2,1)
ketting.insert(1,5)
ketting.delete(4)

ketting.traverse()
print(ketting.retrieve(1))