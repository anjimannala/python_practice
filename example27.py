# to check the given number is abundant number or not
# brutforce
'''num=int(input())
num2=0
for i in range(1,num):
    if num%i==0:
        num2+=i
print("yes" if num2>num else "no")'''
# optimized
'''num=int(input())
num2=1
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        num2+=i
        if num//i!=i:
            num2+=num//i
print("yes" if num2>num else "no")'''

# sum of all digits of a number
'''
def sdn(num):
    sum=0
    while num>0:
        sum+=num%10
        num=num//10
    return sum
print(sdn(int(input())))'''

# sum numbers in the given range

'''
s=int(input())
e=int(input())
sum=0
for i in range(s,e+1):
    sum+=i
print(sum)'''

#method 2
'''start=int(input())
end=int(input())
print((end*(end+1))//2 - ((start-1)*start)//2)'''

#  Find permutations in which n people can occupy r seats in a classroom.

'''
n=int(input())
r=int(input())
num=1
den=1
for i in range(1,n+1):
    num*=i
for j in range(1,(n-r)+1):
    den*=j
print(num//den)'''

'''import math
n=int(input())
r=int(input())
print(math.factorial(n)//math.factorial(n-r))'''

'''n=int(input())
r=int(input())
ans=1
for i in range(n,n-r,-1):
    ans*=i
print(ans)'''
'''n=int(input())
r=int(input())
ans=1
for i in range(n-r+1,n+1):
    ans*=i
print(ans)'''