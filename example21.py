'''1 Given a string, write a program to find the count of Vowels in the string.
   Print "String has more than two vowels" if the count > 2.
   Else print "String doesn't have more than two vowels".

2 Given a number N, write a program that checks if N is not divisible 
   by any number from 2 to 9.
   - Print "Divisible Number" if divisible by any.
   - Print "Indivisible Number" if not divisible.

   Example: N = 15 → Divisible by 3 & 5 → Output: Divisible Number

3 Write a program to check whether the given password is valid or not.
   A valid password must contain:
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one digit

   Example:
   Input: Qwerty00 → Output: Valid Password
   Input: Dashboard → Output: Invalid Password
    '''  

### 1
'''str1=input()
count=0
for i in str1:
    if i in {"a","e","i","o","u"}:
        count+=1
if count>2:
    print("string has more than two vowels" ,count)
else:   
    print("string does not has more than two vowels")'''


### 2
'''n1=int(input())
res=False
for i in range(2,10):
    if n1%i==0:
        res=True
        break
if res:
    print("divisible number")
else:
    print("indivisible number")'''



## 3
'''str3=input()
up,lo,di=False,False,False
for i in str3:
    if i.isupper():
        up=True
    elif i.islower():
        lo=True
    elif i.isdigit():
        di=True
if up and lo and di :
    print("valid password")
else:
    print("invalid password")
'''


#### 4
# input=aaaabbbbaaaahhh
# output=a4b4a4h3
# run length encoded algorithm


str4="aaaabbbcc"
count=1
'''for i in range(7):
    
    if str4[i]==str4[i+1]:
        count+=1
    else:                                                     ### it does not print the last sequense
        print(f"{str4[i]}{count}",end="")
        count=1'''
'''
str4="aabbbbbacta"
count=1
for i in range(1,len(str4)):
    if str4[i]==str4[i-1]:
        count+=1
    else:
        print(f"{str4[i-1]}{count}",end="")
        count=1
print(f"{str4[-1]}{count}")
'''


m=int(input())
n=int(input())

def isprime(num):
    if num<=1:
            return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

list1=[]
for i in range(m,n+1):
    if isprime(i):
         list1.append(str(i))
print(" ".join(list1))

        