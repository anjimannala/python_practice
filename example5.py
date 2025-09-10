'''
strings

collection of characters
syntax
single word='  ----   '
double worda="   -----   "
##multiple lines=




'''


'''
a="i Am Anji"
print(a)
print(type(a))
for i in a:
    print(i,end=" ")

'''
 string operations
lower()
upper()
endswith()
startswith()
replace()
find()   # gives true if else gives -1    
index()    # gives index value if present else gives error
count()
removeprefix()
removesuffix()
split()  # makes string into list
strip()  # removes space
lstrip()  # left space
Rstrip()  # right space



print(a.lower())
print()
print(a.upper())
print()
print(a.endswith("i"))
print()
##print(a.startswith("i"))
b="anji"
b.replace("anji","name")
print(b)

print(a.find("A"))
print(a.index("Anji"))
print(len(a))
print(a.count("A"))
print(a.count("i"))
print(a.count(" "))

b="   i am anji   "
print(b.strip())
print(b.lstrip())
print(b.rstrip())

print(b.strip())

d="i am a eng student"
print(d.split())


c="python language"
print(c.removeprefix("python"))
print(c.removesuffix("language"))
print(c.removeprefix("jfhn"))
print(c.replace("language","programming"))



'''
LIST
list is data structure
syntax  []
mutable data type means modifying
stores different types
it allows duplicates
performs indexing   =>forward indexing(positive)
                    =>backward indexing(negative)

'''
li=[1,2,3,4,4,4,5,6,"anji","self","Manji@10",2.86]
##print(li)
##print(li[0::1])
n=len(li)

##print(li[::-1])
##print()
##print(li[0:n+1:1])
##print(li[0:n+1:2])
##print(li[n+1:5:-1])
##
##print(li[n:0:-1])
##print(li[::-1])


##for i in  li:
##    
##    print(i,end="-")
##for i in li:
##    if i>0:
##        print(i)


LIST OPERATIONS
 append()
 remove()
 insert()
 pop()
 extend()
 reverse()
 index()
 count()


 
##print(li)
##li.append("hdfjsk")
##li.append(678)
##li.append(376.376)
##print(li)
##li.remove("self")
##print(li)
##li.insert(3,"%^&*")
##print(li)
##li.pop(8)
##print(li)
##li.reverse()
##print(li)
##print(li.index("anji"))
##print(li.count(4))
##li.extend([12,8,29,276.65,"hdg"])
##print(li)


## dynamic type of inputing list


##l2=list(map(int,input().split("-")))
##print(l2)




##list comprehension

##l1=[]
##n=int(input())
##res=[i for i in range(n) if i%2==0]
##print(res)
##
##l3=[]
##for i in res[:5:]:
##    l3.append(i)
##    
##print(l3)   










