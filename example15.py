# return statement
'''
a=int(input())
b=int(input())
def add(x,y):
    return x+y       # if no return it return none
c=add(a,b)
print(c)'''


# default arguement

'''def defalt(a,b=10,c=20,d=30):
    return (a+b+c+d)
n=defalt(1)
print(n)
n=defalt(1,2)
print'''
'''
a=int(input())
b=int(input())
def sub(b,a):
    print("a",a)
    print("b",b)
    return a-b       # if no return it return none
c=sub(a,b)
print(c)
'''

# Recusion 
# function calling it self

# factorial 
'''def fact1(n):
   if n==2:
      return 2
   return n*fact1(n-1)
print(fact1(5))
'''
# sum of n natural numbers
'''def sumn(n):
    if n==1:
        return 1
    return n+sumn(n-1)
n=int(input("enter a value:"))
print(sumn(n))'''

'''def add1(n):
    if n==6:
        return 6
    return add1(n+1)
print(add1(1))'''
# fibbonacci series

'''def fib(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input())
for i in range(n):
    print(fib(i))

'''

'''

def fib(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input())
for i in range(n+1):
    print(fib(i))
    
'''


# oops - opject oriented programming system
'''
class iphone:         # class creation
    def icloud(self):
        print("free space")              # methods
    def call(self,num):
        print("calling  ",num)

iphone16=iphone()  # object creation
iphone16.icloud()
num=12896524856
iphone16.call(num)

'''
'''class student():
    def __init__(self,name,roll,branch):   # constructer
        self.name=name
        self.rollno=roll
        self.branch=branch
        print("constructer called")
    def __del__(self):
        print("deestructer called")
s1=student("anji",10,"EEE")
print(s1.name)'''

'''
class amazon():
    def __init__(self):
        self.servicer1=120
        self.servicername="Arjun"
    def complaint(self,customerid,issue):
        print(f"Agent ID:{self.servicer1} Agent Name:{self.servicername} customer Id:{customerid} Issue:{issue}")
complaint=bool(input("complaint?"))
while complaint:
    am=amazon()
    cu_id=int(input("Enter customer Id:"))
    cu_issue=input("Issue:")
    am.complaint(cu_id,cu_issue)
    complaint=False
    '''
'''class AmazonServices:
    def __init__(self,Agentname,agentId,custId):
        self.custId=custId
        self.Agentname=Agentname
        self.agentId=agentId
agentName="sai"
AgentId=12
complaint=input()'''


'''
prinvate members

similar to protected members,the

'''
'''n=int(input())
a=0
b=1
count=1
while count<=n:
    a,b=b,a+b
    count+=1
    if count==n:
        print(b)'''

'''n=int(input())
a=0
b=1
count=2
while count<=n:
    a,b=b,a+b
    count+=1
print(b)'''

## block swap algorithm
'''list1=[1,2,3,4,5]
k=2
temp=0
for i in range(0,k):
    temp=list1[0]
    for j in range(0,len(list1)-1):
        list1[j]=list1[j+1]
    list1[len(list1)-1]=temp
print(list1)'''
# left shift
'''list1=[1,2,3,4,5]
n=len(list1)-1
k=2
temp=0
for i in range(0,k):
    temp=list1[0]
    for j in range(0,n):
        list1[j]=list1[j+1]
    list1[n]=temp
print(list1)'''
# right shift
'''
list2=[10,20,30,40,50,60]
k=3
n=len(list2)-1
temp=0
for i in range(0,k):
    temp=list2[n]
    for j in range(n,0,-1):
        list2[j]=list2[j-1]
    list2[0]=temp
print(list2)'''

# anagram
'''an1=input()
an2=input()
an2=list(an2)
if len(an1)==len(an2):
    for i in an1:
        if i in an2:
            an2.remove(i)
if len(an2)==0:
    print("anagram")
else:
    print("not a anagram")
'''