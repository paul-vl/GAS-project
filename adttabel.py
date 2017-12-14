class tabel:
    content=dict()

    def __init__(self):
        self.content=dict()

    def insert(self,key,val):
        self.content[key]=val

    def remove(self,key):
        self.content.pop(key)

    def retrieve(self,key):
        return self.content.get(key,None)

    def size(self):
        return len(self.content)

    def isempty(self):
        return len(self.content)==0


class queue(tabel):
    #nu is deze inherited van adttabel
    #denk ik

    def __init__(self):
        tabel.__init__(self)
