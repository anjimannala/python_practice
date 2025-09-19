list1=[-2,1,-3,4,-1,2,1,-5,4]
'''list2=[]
subarr=[]
for i in range(len(list1)):
    subarr.append(list1[i])
    for j in range(i+1,len(list1)):
        subarr.append(list1[j])
        list2.append(subarr)
print(list2)'''
# max product of three numbers in a list
'''
list1=[-2,1,-3,4,-1,2,1,-5,4]
list1.sort()
print(list1)
h1=list1[-1]*list1[-2]*list1[-3]
h2=list1[0]*list1[1]*list1[-1]
print(max(h1,h2))

'''




# move zeros to end

'''list2=[1,5,0,8,0,9,3]
list3=[]
for i in list2:
    if i==0:
        list3.append(i)
        list2.remove(i)
list2.extend(list3)
print(list2)
'''
'''
list1=[1,5,0,8,0,9,3]
j=0
for i in range(len(list1)):
    if list1[i]!=0:
        list1[j],list1[i]=list1[i],list1[j]
        j+=1
print(list1)'''
# max sum of a subarray

'''list1=[-2,1,-3,4,-1,2,1,-5,4]
maxsum=list1[0]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if sum(list1[i:j+1]) > maxsum:
            maxsum=sum(list1[i:j+1])
print(maxsum)'''

# for printing with sequence
'''
list1=[-2,1,-3,4,-1,2,1,-5,4]
max=list1[0]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if sum(list1[i:j+1])>max:
            max=sum(list1[i:j+1])
            s=i
            e=j
print(f"subarray {list1[s:e+1]} has the max sum of {max}")

'''
'''
list2=[5,7,9,1,3,2,6]
list2.sort()
h1=list2[-1]*list2[-2]*list2[-3]
h2=list2[0]*list2[1]*list2[-1]
if h2>h1:
    print(f"the three numbers {list2[0],list2[1],list2[-1]} has a max product of {h2}")
else:
    print(f"the three numbers {list2[-1],list2[-2],list2[-3]} has a max product of {h1}")
'''
'''list2=[1,5,0,8,0,9,3]
count=0
for i in list2:
    if i==0:
        count+=1
        list2.remove(i)
list2.extend([0 for i in range(count)])
print(list2)'''
'''list2=[1,5,0,8,0,9,3]
j=0
for i in range(len(list2)):
    if list2[i]!=0:
        list2[i],list2[j]=list2[j],list2[i]
        j+=1

print(list2)
'''
'''def _maxsumofsubarr(nums):
    result=nums[0]
    for i in range(len(nums)-1):
        s=nums[i]
        for j in range(i+1,len(nums)-1):
            result=max(result,s)
            s+=nums[j]
            result=max(result,s)
    return result
list1=[-2,1,-3,4,-1,2,1,-5,4]
print(_maxsumofsubarr(list1))
'''
set1={1,2,3}
set2={1,2,3,4,5}
'''print(set1.union(set2))
print(set2.union(set1))'''
'''print(set1.intersection(set2))
print(set2.intersection(set1))'''
'''print(set1.issubset(set2))
print(set2.issubset(set1))'''
'''print(set1.issuperset(set2))
print(set2.issuperset(set1))'''
'''set1.add(6)
set1.remove(2)

print(set1)'''
dict1={1:2,3:4,"key1":"val1","key2":"val2",1.1:2.2,12:False}

'''print(type(dict1))
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())'''
'''for i in dict1:
    print(dict1[i],end=" ")
dict1.add(5,8)'''


'''
for i,j in dict1.items():
    print(i,":",j)'''


list1=[1,56,7,98,45,24]
'''
for i,v in enumerate(list1):
    print(i,":",v) 

for i,v in enumerate(list1[::-1]):
    print(i,v)

'''

'''list1=["name","branch","roll"]
list2=["anji","eee","224g1a0210"]
for q,a in zip(list1,list2):
    print(f"Q.what is your {q}? A. my {q} is {a}.")
'''
'''for i in reversed(range(1,10,2)):
    print(i)'''
'''
list2=[8,6,1,3,47,1]
for i in sorted(list2):
    print(i)

list2=[8,6,1,3,47,1,5,8,45,10,5]
for i in sorted(set(list2)):
    print(i,end=" ")
'''
import math
'''rd=[45,62,32,56.2,True]
fd=[]
for i in rd:
    if not math.isnan(i):
        fd.append(i)

print(fd)'''

'''print(math.gcd(12,45,60))
print(math.lcm(12,45,60))'''

'''list1=[5,8,3,4,7,6,3,2,1,1,2,5,8,8,8]
set1=set(list1)
dit={}
for i in set1:
    dit[i]=list1.count(i)

list2=[]
for num,freq in dit.items():
    list2.append((-freq,num))
list2.sort()
print(list2)
final=[]
for freq,num in list2:
    final.extend([num]*(-freq))
print(final)'''
'''
list1=[5,8,3,4,7,6,3,2,1,1,2,5,8,8,8]
set1=set(list1)
dit={}
for i in set1:
    dit[i]=list1.count(i)

list2=[]
for num,freq in dit.items():
    list2.append((freq,num))
list2.sort(reverse=True)
print(list2)
final=[]
for freq,num in list2:
    final.extend([num]*(freq))
print(final)'''

from collections import Counter

'''list1=[5,8,3,4,7,6,3,2,1,1,2,5,8,8,8]
list2=[]
dit=Counter(list1)
for num,freq in dit.items():
    list2.append((-freq,num))
list2.sort()'''
'''print(list2)
final=[]
for freq,num in list2:
    final.extend([num]*(-freq))
print(final)'''
'''
import math
num=5
print(math.factorial(num))
'''
'''s=open("demo.txt",mode="r")
print(s.read())
s.close()
'''
'''d=open("demo.txt",mode="w")
d.write("yes i am there")
d.close()

f=open("demo.txt",mode="a")
f.seek(0)
f.write(" gchjdk")'''

'''g=open("demo.txt",mode="r+")
print(g.read())
#g.seek(0)
g.write("fghj")
g.seek(0)
print(g.read())
'''
'''f=open("demo.text",mode="w+")
f.write("erty")
f.seek(0)
print(f.read())
f.write("yj")
f.close()'''
s=open("demo.txt",mode="w")
s.write("empty file")
s.close()