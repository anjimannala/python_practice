'''n=5
for rows in range(1,n+1,1):
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range (1,rows+1,1):
        if cols==1 or cols==rows or rows==n:
            print(cols,end=" ")
        else:
            print(" ",end=" ")
    print()'''
###  functins 
# block of code which is reusable and for a specific one
# argument and parameters
'''
positional arguements
named arguments
relational arguments
identical arguments

'''

# check weather given no. is amstrong num or not
# means  sum of ower of each digit in a number is the given num
# 1=123
# 1**3 +2**3 + 3**3 == 123
#1234
#1**4 +2**4+3**4+4**4


# amstrong
# perfect number   n=6 multiples sum shoud be the n 1+2+3=6
# anagram  1234=3124

'''
n=str(input())
power=len(n)
sum=0
for i in n:
    sum+=int(i)**power
if sum==int(n):
    print("Amstrong")
else:
    print("Not Amstrong")
'''
'''n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("Not perfect number")

'''
'''n1=str(11234)
n2=str(12344)
is_anagram=True
if len(n1)==len(n2):
    for i in n1:
        if i in n2:
            break
        else:
            is_anagram=False
if is_anagram:
    print("anagram")
else:
    print("not anagram")'''
'''n=int(input())
is_prime=True
if n<=0:
    print(f"{n} is not prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
    if is_prime:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
'''

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
'''n=int(input("Enter a value:"))
if is_prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not a prime")
'''

'''n=int(input("enter a range:"))
i=2
while i<=n:
    if  is_prime(i):
        print(i,end=" ")
    i+=1
'''

'''n=int(input("how many primes from starting:"))
i=0
count=1
while count<=n:
    if  is_prime(i):
        print(i,end=" ")
        count+=1
    i+=1

'''

'''n=int(input())
tr=list(map(int,input().split(" ")))
p,s,no=0,0,0
for i in tr:
    if i>0:
        p+=1
    elif i<0:
        s+=1
    elif i==0:
        no+=1
print(p,s,no)'''


# count the frequency of each element in a list

'''list_1=list(map(int,input("enter a list:").split(" ")))
set_1=set(list_1)
for i in set_1:
    print(f"{i}'s count in list is {list_1.count(i)}")'''

# increase and decrase order

'''list1=[4,8,6,2,7,3,1]
list1.sort()
n=len(list1)//2
print(list1[:n:] + list1[-1:n-1:-1])'''


# sum of elements in the array
'''list2=[4,8,6,2,7,3,1]
sum=0
for i in list2:
    sum+=i
print(sum)'''

# block swap algorithm
list2=[4,8,6,2,7]
'''n=5
k=2
a=list2[:k:]
b=list2[k::]
print(a)
print(b)
'''

list2=[4,4,5,5,556,7,1]
'''sum=0
for i in list2:
    sum+=i
print(sum/len(list2))
'''
