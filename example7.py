## SET
'''
it is a sequential data type
the syntax is represented like as dictionary with flower bracs  {   }
based upon data it acts as set
do not allow duplicate data elements
no indexing and slicing
do not allow mutable data elements
it is unordered means randomly prints or adds in to the set
iteration is allows

there are several set methods'''
## SET METHODS
'''
> add()    add to the set
> update()  change or modify
> pop()   removes element randomly
> remove()'''

## SET OPERATIONS
'''
> union()
> intersection()
> differnce()
> subset()
>superset()
'''
##s1={}
##print(type(s1))
s2={1,3,"ydgewui"}
##print(type(s2))
##print(s2)

s2.add(4)
##print(s2)
##s2.update("egdfg")
##print(s2)

##s2.pop()
##print(s2)

##s2.remove(3)
##s2.remove("ydgewui")
##print(s2)

## union
 #it adds two set by removing duplicates
'''
a={1,2,3,4,5}
b={4,5,6}
print(a,type(a))
print(b,type(b))

c=a.union(b)
print(c)
d=b.union(a)
print(d)
'''
## INTERSECTION
## it prints only same elements in two sets
'''
a={1,2,3,4,5}
b={4,5,6}

c=a.intersection(b)
print(c)

d={6,7}
e=b.intersection(a,b)
print(e)'''

## DIFFERENCE
## it print the elements in A only  not present in B
'''
a={1,2,3,4,5}
b={4,5,6,8}
print(a.difference(b))
print(b.difference(a))'''

## SUBSET
# if elements in b present in a then it is called b is subset of a
'''
a={1,2,3,4,5,6}
b={4,5,6}
print(b.issubset(a))
print(a.issubset(b))
'''
## SUPERSET
# similarly call it is as a is superset of b because a contains all elements in b

'''
a={1,2,3,4,5,6}

b={4,5,6}
print(a.issuperset(b))
print(b.issuperset(a))
'''
## ITERATION

a={1,2,3,4,5,6}
b={4,5,6}
for i in a:
    print(i,end=" ")


for i in b:
    if i%2==0:
        print(i)
        
i =int(input())




























































