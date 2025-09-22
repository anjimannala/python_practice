# palindrome


def isreverse(n):
    rev=0
    rem=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev


def ispalindrome(n):
    if n==isreverse(n):return True
    else:return False
'''
n=int(input())
if ispalindrome(n):print("Palindrome")
else:print("Not a palindrome")'''

# range of palindromes

'''n=int(input())
m=int(input())
for i in range(n,m+1):
    if ispalindrome(i):
        print(i,end=" ")'''

#n=str(input())
'''def isamstrong(n):
    am=0
    for i in n:
        am+=int(i)**len(n)
    return am'''


'''if int(n)==isamstrong(str(n)):print("Amstrong")
else:print("not a amstrong")'''


'''
def isamstrong(n):
    am=0
    count=len(str(n))
    while n>0:
        am+=(n%10)**count
        n=n//10
    return am
n=int(input())
if n==isamstrong(n):print("Amstrong")
else:print("not a amstrong")'''

# sum ao arithmetic progression series

'''a=int(input("Enter starting value: "))
d=int(input("Enter common difference: "))
n=int(input("Enter no of terms: "))
count=1
list1=[a]
while count < n:
    a+=d
    list1.append(a)
    count+=1
print(list1)
print(sum(list1))'''
'''
a=int(input("Enter starting value: "))
d=int(input("Enter common difference: "))
n=int(input("Enter no of terms: "))
count=1
sum=a
while count < n:
    a+=d
    sum+=a
    count+=1
print("sum : ",sum)
'''


# using Formulae
'''a=int(input("Enter starting value: "))
d=int(input("Enter common difference: "))
n=int(input("Enter no of terms: "))
sum=a
while n>1:
    a+=d
    sum+=a
    n-=1
print("sum : ",sum)

'''
'''a=int(input("Enter starting value: "))
d=int(input("Enter common difference: "))
n=int(input("Enter no of terms: "))
sum=n/2*(2*a+(n-1)*d)
print(int(sum))'''

## geometric progression sum
# the sequence which is change or different commom difference called common ratio


# using iterative method
'''
a=int(input("Enter starting value: "))
r=float(input("Enter common ratio: "))
n=int(input("Enter no of terms: "))
sum=0
for i in range(n):
    sum+=(a)*(r)**i
print(sum)'''

# using formulae

'''a=int(input("Enter starting value: "))
r=float(input("Enter common ratio: "))
n=int(input("Enter no of terms: "))
sum=a*((r**n)-1)/(r-1)          
print(sum)'''                            


# greatest of three numbers
'''
a,b,c=map(float,input().split())
if a > (b and c):
    print(a,"is greater")
elif b > (a and c):
    print(b,"is greater")
else:
    print(c,"is greater")
'''

# to print the given year is leap year or not

'''
y=int(input())
def isleap(y):
    if (y%4==0 and y%100!=0) or y%400==0:
        return True
    return False
if isleap(y):print("leap year")
else:print("not a leap year")
'''

# to find the max and min digit in number

'''num=int(input())
for i in str(num):
    if i is max(str(num)):
        maxd=i
    if i is min(str(num)):
        mind=i

print(maxd,mind)
print(max(str(num)),min(str(num)))'''
'''
num=input()
for i in str(num):
    if i is max(num):
        maxd=i
    if i is min(num):
        mind=i

print(maxd,mind)
print(max(num),min(num))
'''
# with normal iterative method

'''num=int(input())

def is_maxd_mind(num):
    if num<0:
        num=-num
    if num==0:
        return 0,0
    largest=0
    smallest=9
    while num>0:
        digit=num%10
        largest=max(largest,digit)
        smallest=min(smallest,digit)
        num=num//10
    return largest,smallest
print(is_maxd_mind(num))
'''

# power of the number
'''
x,p=map(int,input().split())
res=1
for i in range(1,p+1):
    res*=x
print(res)'''


# efficient method

### Inefficient Method (Iterative Multiplication)
'''
This is the simplest, most intuitive approach, but it's slow for large exponents.

```
FUNCTION PowerIterative(x, p):
  // Initialize result to 1
  SET result = 1

  // Loop 'p' times
  FOR i FROM 1 TO p:
    // Multiply result by x in each iteration
    SET result = result * x

  // Return the final result
  RETURN result
'''
### Efficient Method (Binary Exponentiation)

'''This method is significantly faster for large exponents because it uses the binary representation of `p`.

```
FUNCTION PowerBinary(x, p):
  // Initialize result to 1
  SET result = 1

  // Loop while the exponent 'p' is greater than 0
  WHILE p > 0:
    // Check if 'p' is odd (the last bit is 1)
    IF p is ODD:
      // If odd, multiply the result by the current 'x'
      SET result = result * x

    // Square the base 'x' for the next iteration
    SET x = x * x

    // Halve the exponent 'p' (integer division)
    SET p = p / 2

  // Return the final result
  RETURN result'''
num=int(input())
p=int(input())
res=1
while p>0:
    if p%2==1:
        res=res*num
    num=num*num
    p=p//2
print(res)