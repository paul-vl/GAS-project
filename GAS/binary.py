class binary_boom():
    def __init__(self,rootitem=None,parent=None,linkerboom=None,rechterboom=None):
        """
        node ineens initen in de binaire boom
        :param rootitem: item op knoop
        :param linkerboom: linkerboom van self
        :param rechterboom: rechterboom van self
        """
        self.linkboom=linkerboom
        self.rechterboom=rechterboom
        self.rootitem=rootitem

    def isempty(self):
        if self.rootitem!=None:
            return 0
        else:
            return 1

    def getlength(self):
        """
        geeft lengte van de inorder terug, effectief de lengte van het boom
        :return: ..
        """
        return len(self.inorder())

    def insert(self,item):
        """
        voeg een item toe in binaire zoekboom
        :param item:item to insert
        :return: succes or not
        """
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
        """
        :return: lijst met alle elementen gerangschikt van klein naar groot
        """
        a=[]
        if self.linkboom!=None:
            a=a+self.linkboom.inorder()
        a.append(self.rootitem)
        if self.rechterboom!=None:
            a=a+self.rechterboom.inorder()
        return a


    def retrive(self,index):
        """
        :param index:positie
        :return: geeft de index-de kleinste element
        """
        return self.inorder()[index-1]

    def find_inordersuccesor(self,item):#non public internal function.
        a=self.inorder()
        for index,i in enumerate(a):
            if i==item:
                return a[index+1]

    def delete(self,item,parent=None,links=None):
        """
        :param item:item to delete
        :param parent: from where does the recursion calls(internal)
        :param links: left or right call(internal)
        :return: succes or not
        """
        if item==self.rootitem:#item found
            if self.linkboom==None and self.rechterboom==None:
                #dat is blad, gewoon verwijderen.
                if links==1:
                    parent.linkboom=self.linkboom
                if links==0:
                    parent.rechterboom=self.linkboom
                return True
            elif self.rechterboom!=None:
                #er is een inorder succesor, swap deze en verwijder de inordersuccesor in de deelboom
                succesor=self.find_inordersuccesor(item)
                self.rootitem=succesor
                return self.rechterboom.delete(succesor,self,0)
            else:
                #er is geen rechterboom, delete en laat de linkseboom de plaats in nemen
                if links==1:
                    parent.linkboom=self.linkboom
                if links==0:
                    parent.rechterboom=self.linkboom
                return True
        if item>self.rootitem:
            #rechts recursion
            if self.rechterboom==None:
                return False
            else:
                self.rechterboom.delete(item,self,0)
        elif item<self.rootitem:
            #linkse recursion
            if self.linkboom==None:
                return False
            else:
                self.linkboom.delete(item, self,1)
#some test
if __name__=="__main__":
    cc=binary_boom(5)
    cc.insert(2)
    cc.insert(1)
    cc.insert(50)
    cc.insert(20)
    cc.insert(25)
    print(cc.inorder())
    print(cc.retrive(2))
    cc.delete(2)
    print(cc.inorder())
    cc.delete(5)
    print(cc.inorder())
    print(cc.retrive(2))
    print(cc.getlength())
    print(cc.isempty())
