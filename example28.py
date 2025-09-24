# WAP to replace all 0's with 1 of an integer
'''
num1=list(input())
for i in range(len(num1)):
    if int(num1[i])==0:
        num1[i]=1
print(*num1,sep="")'''

'''num2=int(input())
ans,temp=0,1
while num2>0:
    d=num2%10
    if d==0:
        d=1
    ans=temp*d+ans
    temp*=10
    num2//=10
print(ans)'''

'''
def isPrime( n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if n and (n - 2) are both prime
def prime( n):
    return isPrime(n) and isPrime(n - 2)
n = int(input())
if prime(n):
    print("Yes")
else:
    print("No")'''

#wap to check the given number is sum of two prime numbers
'''def isprime( n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def sum_primes(num):
    # num =p1 + p2
    # the we need to check the p1 and p2 are primes gy iteraton
    for i in range(2,num//2 +1):
        if isprime(i):
            if isprime(num-i):
                return True
    return False
num=int(input())
print("yes" if sum_primes(num) else "no")'''


# wap to find the area of the circle
'''r=float(input())
res=r*(22/7)
print(f"{res:.3f}")'''