'''name="anji"
name[0]='S'
print(name)   #which is immutable in individual'''
'''name1="all silver tea cups"
print(name1.title())
name1=name1.split()
print(name1)
for i in name1:
    print(i[0].upper()+i[1:],end=" ")'''
str1="All silver Tea cups"
'''str1=str1.capitalize()
for i in range(len(str1)):
    if str1[i]==" " and  str1[i+1]!= " ":
        str1=str1[:i+1]+str1[i+1].upper()+str1[i+2:]
print(str1)'''
'''nums="1 2 3 4"
list1=nums.split()
print(list1)
list2=str1.split()
print(list2)
list2=str1.split("a")
print(list2)
str3="a".join(list2)
print(str3)'''
'''list4=str1.lower().split()
str4="_".join(list4)
print(str4)'''
'''list5=str1.title().split()
list5="".join(list5)
print(list5)'''
'''list6=str1.title().split()
str6="".join(list6)
print(str6[0].lower()+str6[1:])'''
'''list7=str1.title().split()
str7="-".join(list7)
print(str7)'''
'''count=0
vow=input("enter any string : ").lower()
for i in vow:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
print("total no.of vowels:",count)'''
'''count=0
for i in vow:
    if i in "aeiou":
        count+=1
print("total no.of vowels:",count)'''

name5="Anji"
name2=""
'''#print(name5.swapcase())
for i in name5:
    if i.islower():
        name2+=i.upper()
    else:
        name2+=i.lower()
print(name2)
'''
lis=[23,8,1,0,5,45]
'''large=0
print(lis)
for i in lis:
    if i>large:
        large=i
print(large)
lis.sort()
print(lis)
print(lis[-1])
lis.sort(reverse=True)
print(lis)
print(lis[0])'''
'''lis2=sorted(lis)
print(lis2)
print(lis2[-1])
lis3=[1,2,5,6,8]
res=[i for i in lis3 if i>2]
print(res)'''
'''l1=input("Enter values:").split()
l2=sorted(l1)
print(l1)
# map(name of the function,varible_name) to convert elements in list tnto integers
map(int,l2)
print(l2)
l3=list(map(int,input().split(",")))
print(l3)
'''
'''lis=[23,8,1,0,5,45,8,7]
large=lis[0]
print(lis)
for i in lis[1::]:
    if i>large:
        large=i

print("largest ",large)
'''
'''lis=[23,8,1,0,5,45,8,7,-5]
small=lis[0]
for i in lis:
    if i<small:
        small=i
print("smallest ",small)'''
'''lis=[3,8,1,0,5,45,28,8,7,26]
large=lis[0]
print(lis)
slarge=0
for i in lis[1::]:
    if i>large:
        slarge=large
        large=i
    elif i>slarge:
        slarge=i
print("second largest ",slarge)'''
'''lis=list(map(int,input("Enter values: ").split(" ")))
large=lis[0]
print(lis)
slarge=0
for i in lis[1::]:
    if i>large:
        slarge=large
        large=i
    elif i>slarge:
        slarge=i
print("second largest ",slarge)'''
'''n=int(input("enter a value:"))
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''



