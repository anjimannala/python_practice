'''list1=[8,8,"hgj",526.8, True]
list1.append(4)
print(list1)
list1.pop(0)
list2=[5,9,"gfdh"]
list1.extend(list2)
print(list1)
print(list1.count(8))
print(list1.index(True))
list1.Replace(852,7)
print(list1)'''

'''s="programming"
v=0
c=0
for i in s:
    if i in ("a","e","i","o","u"):
        v+=1
    else:
        c+=1
print(v,c)'''
### median of a list of elements

'''list2=[1,2,3,6,7,8,9,4,5]
list2.sort()
print(list2)
lenth=len(list2)
median=0
if lenth % 2 ==0:
    median=(list2[lenth//2]+list2[(lenth//2)-1] )/2
else:
    median=list2[lenth//2]
print(median)'''


'''list2=[1,2,3,6,7,8,9,4,5,10]
list2.sort()
print(list2)
lenth=len(list2)
median=0
if lenth % 2 ==0:
    median=(list2[lenth//2]+list2[(lenth//2)-1] )/2
else:
    median=list2[lenth//2]
print(median)'''


##
'''n=int(input())
a=0
b=1
list3=[]
list3.extend([a,b])
#print(list3)
for i in range(n-2):
    a,b=b,a+b
    list3.append(b)
print(list3)'''

'''n=int(input())
a=0
b=1
list3=[]
list3.extend([a,b])
#print(list3)
for i in range(n-2):
    a,b=b,a+b
    list3.append(b)
print(list3)

print("even seq of fib ",[i for i in list3 if i%2==0])
print("odd seq of fib ",[i for i in list3 if i%2!=0])

'''
'''n=int(input())
a=0
b=1
print(a,b,end=" ")
while b<n:
    a,b=b,a+b
    print(b,end=" ")
'''
'''m=int(input())
n=int(input())
a=0
b=1
if m<=0:
        print(a,end=" ")
if m<=1:
     print(b,end=" ")
while b<n:
    a,b=b,a+b
    if m<=b and n>=b :
        print(b,end=" ")'''
'''n=20   
a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
     a,b=b,a+b
     print(b,end=" ") 
'''
#output=0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181


'''def fib(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input())
for i in range(n+1):
    print(fib(i))
    '''

'''def isprime(n):
    if n<=0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
'''

'''n=input()
if isprime(n):
    print("prime")
else:
    print("not prime")'''
'''
m=int(input())
n=int(input())
for i in range(m,n+1) :
    if isprime(i):
        print(i ,end=" ")
    #else:
      #  print("not prime")'''


'''list3=list(map(int,input().split()))
set3=set(list3)
mode=0
count=0
for i in set3:
    if list3.count(i)>count:
        count=list3.count(i)
        mode=i
print(mode ,"is mode")'''
'''n=10
li=[(i,j,k) for i in range(2) , j for j in range(2) k for k in range(2) if (i+j+k)==3]
print(li)'''


def isprime(number,div=2):
    if number==div:
        return True

    if number%div==0:
        return False
    return isprime(number,div+1)
#
'''for i in range(2,n+1):
    if isprime(i):
        print(i)
'''
'''n=10
count=1
i=2
while n>=count:
    if isprime(i):
        print(i,end=" ")
        count+=1
    i+=1'''

i=int(input())
n=int(input())
count=1
while n>=i:
    if isprime(i):
        print(i,end=" ")
        count+=1
    i+=1