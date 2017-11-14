class binary_boom():
    def __init__(self,rootitem=None,parent=None,linkerboom=None,rechterboom=None):
        self.linkboom=linkerboom
        self.rechterboom=rechterboom
        self.rootitem=rootitem
        self.parent=parent
    def insert(self,item):
        if item>=self.rootitem:
            if self.rechterboom==None:
                self.rechterboom=binary_boom(item,self)
            else:
                self.rechterboom.insert(item)
        elif item<self.rootitem:
            if self.linkboom==None:
                self.linkboom=binary_boom(item,self)
            else:
                self.linkboom.insert(item)

    def inorder(self):
        a=[]
        if self.linkboom!=None:
            a=a+self.linkboom.inorder()
        a.append(self.rootitem)
        if self.rechterboom!=None:
            a=a+self.rechterboom.inorder()
        return a

    def retrive(self,knoop):
        return self.inorder()[knoop]

    def find_inordersuccesor(self,item):
        a=self.inorder()
        for index,i in enumerate(a):
            if i==item:
                return a[index+1]

    def delete(self,item,parent=None,links=None,rechts=None):
        if item==self.rootitem:
            print("found")
            if self.linkboom==None and self.rechterboom==None:
                print("blad verwijderd")
                if links==1:
                    parent.linkboom=self.linkboom
                if rechts==1:
                    parent.rechterboom=self.linkboom
                return True
            elif self.rechterboom!=None:
                print("!")
                succesor=self.find_inordersuccesor(item)
                self.rootitem=succesor
                return self.rechterboom.delete(succesor,self,0,1)

            else:
                print("done?")
                if links==1:
                    parent.linkboom=self.linkboom
                if rechts==1:
                    parent.rechterboom=self.linkboom
                return True
        if item>self.rootitem:
            if self.rechterboom==None:
                print("rechts niet gevonden")
                return False
            else:
                print("rechts")
                self.rechterboom.delete(item,self,0,1)
        elif item<self.rootitem:
            if self.linkboom==None:
                print("links niet gevonden")
                return False
            else:
                print("links")
                self.linkboom.delete(item, self,1)
cc=binary_boom(5)
cc.insert(2)
cc.insert(1)
cc.insert(50)
cc.insert(20)
cc.insert(25)
print(cc.inorder())
print(cc.retrive(2))
cc.delete(2)
cc.delete(5)
print(cc.inorder())
