#TUPLE
'''
data type
> syntax=()
> allows different type of elements
> allows duplicates
> indexing and slicing like a list
> it is a immutable data type
> there are no methods only contains some built in functions
   min(),max(),sum(),fact(), len()
'''
'''a=()
print(type(a))
b=(1)
print(type(b))
a=(1,2,3,4,5.67,"ramu",[9,8,9.65,"list"])
print(a)
print(type(a))
for i in a:
    print(type(i))
    print(i)
print(a[4])
print(a[0::])
a[4]=365
print(a[::-1])
print(len(a))
a=(1,2,3,4.65,9)
print(min(a))
print(max(a))
print(sum(a))
n=len(a)
print(a[n:0:-1])
print(a[::])'''
####TUPLE OPERATIONS
##>concatenation    adds two tuples
##>iteration    for,while
##>membership operation    in=checks weather its present True or False
##> identify operation      is ,is not compare two tuples
##> repetion  
'''
t1=(1,2,3,4,5.67)
t2=(9,8,7,6.54)
t3=(1,2,3,4,5.67)
print(t1+t2)
i=0
while i<n:
    print(a[i])
    i+=1

for i in a:
    print(a[i])

i=int(input())
print(t1*i)
print(t2*3)

print(2 in t2)
print(1 in t1)
print(t1 is t2)
print(t1 is not t2)
print(t2 is t1)
print(t3 is t1)
'''


##  DICTIOANRY
'''
it is sequential data type

syntax {key1:value1,key2:value2  -------}
key is immutable and acts as list
value is mutable
key is acts as a index to access
keys are must be unique
'''
a={1:"anji","m":123,12.3:(1,2,3),"shdg":[136,"ygfu"],1:23}
##print(a)
##print(a.get(1))
##b=a.get("shdg")
##print(b)
##print(type(b))


'''
a.update({23:8786})
print(a)
print(a.values())
print(a.keys())
m=a.items()
print(m)
print(type(m))
for i in a.items():
    print(i)
'''



























