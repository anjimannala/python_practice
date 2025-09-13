'''#1
name= input("enter name:")
l=len(name)-1
f=0

while f<l:
    if name[f]==name[l]:
        res="palin"
        f+=1
        l-=1
    else:
        res="not palin"
        break

print(res)
# 2
name1=""
for i in range(0,len(name)-1,1):
    name1=name[i]+name1
if name==name1:
    print("palin")
else:
    print("not palin")
#3
name1=""
for i in range(len(name)-1,-1,-1):
    name1+=name[i]
if name==name1:
    print("palin")
else:
    print("not palin")
# to check only half
name= input("enter name:")
l=len(name)-1
f=0
while f<=l:
    if name[f]==name[l]:
        res="palin"
        f+=1
        l-=1
    else:
        res="not palin"
        break

print(res)
n1=int(input())
count=0
for i in range (2,n1,1):
    if n1%i==0:
        count+=1

if count==0:
    print("prime")
else:
    print("not prime")'''
'''n2=int(input())
is_prime=True
for i in  range(2,n2):
    if n2%i==0:
        is_prime=False
print("prime" if is_prime else "not prime")
'''
import math
n2=int(input())
is_prime=True
for i in  range(2,int(math.sqrt(n2)+1)):
    if n2%i==0:
        is_prime=False
print("prime" if is_prime else "not prime")
