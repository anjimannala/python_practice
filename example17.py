'''# inheritance

# single level inheritance
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello")
class child(parent):
    def sound(self):
        print(f"i am {self.name} my age is {self.age}")
c1=child("anji",21)
c1.greet()
c1.sound()



# multilevel inheritance

class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello")
class child(parent):
    def sound(self):
        print(f"i am {self.name} my age is {self.age}")

class subchild(child):
    def greet(self):
       print( f"i am sub child of {self.name} my age is {self.age}")
c2=subchild("anji",21)
c2.greet()

# multiple inheritance

# single child multiple parents

# hirarchial inheritance   = singel parent multiple childs


#Single level

class Parent:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello")

class Child(Parent):

    def sound(self):
        print(f"I'm {self.name}")


#hierarchical

class Child2(Parent):

    def sound(self):
        print("hierarchical inheritence")
    
    def car(self):
        print("I'm having lambo")


#Multiple, multi-level

class Grandchild(Child,Child2):

    def sound(self):
        print(f"I'm {self.name}, implementing multi level inheritence")

c1 = Grandchild("rahul",1)
c1.sound()


# encapsulation

class Bank:

    def __init__(self,acc,balance):
        self.acc = acc
        self.__balance = balance
        print(self.acc,"account created successfully")

    def get_balance(self):
        print("your ",self.acc,"account balance",self.__balance)

    def set_balance(self,amount):
        self.__balance +=amount

kotak = Bank("saving",1000)
kotak.set_balance(2000)
kotak.get_balance()
sbi=Bank("current",1234)
sbi.set_balance(1234)
sbi.get_balance()

c3 = Child("ram",21)
c4 = Child2("hari",20)
c3.sound()
c4.sound()

# abstraction
from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def b(self):
        pass
class bmw(car):
    def b(self):
        print("breaks applied")
car1=bmw()
car1.b()



#examples
class Phone:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def mobile(self):
        print(f"This is {self.brand} {self.model}")


class Vivo(Phone):

    def call(self):
        print(f"Calling from {self.brand} ...")

class Iqoo(Phone):

    def call(self):
        print(f"Calling from {self.brand} ...")

class Bank:

    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)
    
    def set_balance(self,amount):
        self.__balance +=amount

kotak = Bank("Tharun",1000)
kotak.get_balance()
kotak.set_balance(500)
kotak.get_balance()


from abc import ABC,abstractmethod

class Sim(ABC):

    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def call(self):
        pass

    def sms(self):
        print(f"SMS sent Successfully by {self.name}")

#s1 = Sim("jio")
#s1.sms()


class NegativeWithdraw(Exception):
    pass

balance = 1000

try:
    withdraw = int(input())
    if withdraw>balance:
        raise NegativeWithdraw("Insufficient funds")
except NegativeWithdraw as e:
    print("Error",e)
        
''''''
class parent():
    def __init__(self):
        self.name="asdf"
        self.roll=123
    def sound1(self):
        print("parent sound")
class child(parent):

    def sound(self):
        print("child sound")
c1=child()
c1.sound1()

'''
# finding repeated elements inlist
'''list1=[1,2,3,4,5,1,2,4]
duplist=[]
frequency={}
for i in list1:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for i,count in frequency.items():
    if count>1:
        duplist.append(i)

print(duplist)'''



'''list1=[1,2,3,4,5,1,2,4]
set1=set(list1)
list2=[]
for i in set1:
    if list1.count(i)>1:
        list2.append(i)
print(list2)'''

'''list1=[1,2,3,4,5,1,2,4,8,9,8,1,0,6,45]
set1=set(list1)
list2=[]
for i in set1:
    if list1.count(i) ==1 :
        list2.append(i)
print(list2)
'''
'''list3=[4,7,56,0,28,100]
list4=sorted(list3)
print(list4)
for i in list3:
    print(list4.index(i),end=" ")

'''
'''list1=[1,2,3,4,5,1,2,4,8,9,8,1,0,6,45,45,45]
freq={}
set1=set(list1)
print(set1)
for i in set1:
    
print(freq)'''


'''list1=[1,2,3,4,5,1,2,4,8,9,8,1,0,6,45,45,45]
set1=set(list1)
freq=[]
for i in set1:
    freq.append(list1.count(i))
print(list(set1))
print(freq)'''
'''
lop=[(1,2),(5,4),(2,1),(4,5),(3,7),(7,3)]
print(lop)
for i in range(len(lop)-1):
    x1,y1=lop[i]
    for j in range(i+1,len(lop)):
        x2,y2=lop[j]
        if x1==y2 and x2==y1:
            print(f"{lop[i]} is subpair of {lop[j]}")
'''
n=int(input())
l1=[]
for i in range(n+1):
    l1[i]=input()
