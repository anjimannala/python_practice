def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

##n=int(input())
##print("prime numbers are: ",end="")
##for i in range(2,n+1):
##    if is_prime(i):
##        print(i,end=" ")
def firstNPrimes():
    n=int(input())
    primes=[]
    num=2
    while len(primes)<n:
        if is_prime(num):
           primes.append(num)
        num+=1
    return primes
a=firstNPrimes()
print(a)
b=[i for i in a if i%2==0 ]
c=[i for i in a if i%2!=0 ]
print(f"even prime nums : {b}")
print(f"odd prime nums : {c}")
print(sum(c))
print("odd primes : ",end="")
for i in b:print(i,end=" ")


































    


