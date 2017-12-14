from adttabel import *
#from gebruiker import *

class gebruiker:
    pass

class stack:
    content=[]

    def __init__(self):
        self.content=[]

    def insert(self,val):
        self.content.append(val)

    def remove(self):
        self.content.pop(len(self.content)-1)

    def retrieve(self):
        if len(self.content)!=0:
            return self.content[len(self.content)-1]
        return None

class queue:
    pass


def ordermenu(user):
    pass

if __name__ =="__main__":

    user=tabel()
    worker=stack()
    bestellingen=queue()

    while True:
        print("Welkom to Quetzal, 1)login with existing user id, 2)register")
        command=input("please input command")
        while command != 1 and command != 2:
            print("please input a correct command")
            command = input(" 1)login with existing user id, 2)register")
        if command==1:
            username=input("please give me your username")
            useraccount=user.retrieve(username)
            if useraccount!=None:
                print("login succesful, going to the order menu now...")
                ordermenu(useraccount)
            else:
                print("this username doesn't exist, please check the capital letters and typos and try again, or register as a new user")
                break
        elif command==2:
            print("registering new user")
            firstname=input("what's your first name?")
            lastname=input("what's your last name?")
            email=input("what's your email adress?")
            adress= input("And your adress?")
            username= input("which username do you want to use?")
            print("completing registration")
            user.insert(username,gebruiker(firstname,lastname,email,adress,username))#need to be implemented
            print("you can now login with your username")
            break

