#### min and max digits of a given number
'''
num = int(input())
rev=0
mind=9
maxd=0
while num>0:
    if num<0:
        print(0,0)
    rev=num%10
    mind=min(mind,rev)
    maxd=max(maxd,rev)
    num=num//10
print(mind,maxd)
'''
# GCD (greatest common divisor ) of two numbers
'''
num1=int(input())
num2=int(input())
gcd=1
div=1
while div <= min(num1,num2):
    if num1%div==0 and num2%div==0:
        gcd=div
    div+=1
print(f"gcd={gcd}")'''

'''
num1=int(input())
num2=int(input())
div= min(num1,num2)
while div >=1:
    if num1%div==0 and num2%div==0:
        print(f"gcd={div}")
        break
    div-=1'''
'''num1=int(input())
num2=int(input())
def gcd_(num1,num2):
    while num2:
        num1,num2=num2,num1%num2
    return num1
def lcm_(num1,num2):
    if (num1 and num2)==0:
        return 0
    else:
        return (num1*num2)//gcd_(num1,num2)
print(lcm_(num1,num2))'''
# LCM least coomon multiple of two numbes
'''
num1=int(input())
num2=int(input())
mul=max(num1,num2)
i=2
while mul:
    if mul%num1==0 and mul%num2==0:
        print("LCM:",mul)
        break
    mul*=i
    i+=1
'''
# to check the given number is automorphic or not
'''
num=int(input())
if str(num*num).endswith(str(num)):
    print(1)
else:print(0)'''
'''num=int(input())
res=False
num1=num*num
while num>0:
    if num%10==num1%10:
        res=True
    else:res=False
    num=num//10
    num1=num1//10
print(1 if res else 0)'''

# to check the given number is harshad number or not

# string approach

'''num1=int(input())
sum1=0
for i in str(num1):
    sum1+=int(i)
print(1 if num1%sum1==0 else 0)'''

# brutforce approach
'''num1=int(input())
og=num1
sum1=0
while num1!=0:
    sum1+=num1%10
    num1=num1//10
if og%sum1==0:
    print("yes")
else:
    print("no")'''




