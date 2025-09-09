'''
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return "Not Prime"  
    return "Prime"
while True:
    n = int(input("Enter a value:"))
    print(prime(n))


def prime(i):
    for j in range(2,n):
        if i%j==0:
            return 0
    return 1

n=int(input("Enter a value:" ))
l1=[]

n=int(input())
l1=[i for i in range(n+1) if i%2==0]
print(l1)
'''
def prime(n):
    for i in range(2,n+1):
        if n%i==0:
            return 0  
    return 1
n=int(input())
l1=[]

for i in range(2,n+1):
    if prime(i)==1:
        l1.append(i)
    
print(l1[0:n])    
