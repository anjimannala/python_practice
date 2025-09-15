# to find unique
'''list_1=list(map(int,input("enter a list:").split()))
fsum=sum(list_1)
ssum=sum(set(list_1))*2
res=ssum-fsum
print("unique:",res)'''


# factorial
'''n=int(input())
fact=1
for i in range(n,1,-1):
    fact*=i
print(fact)'''


'''n1=int(input())
sum=0
for i in range(1,11,1):
    print(n1*i,end=" ")
    sum=sum+n1*i
print()
print(sum)'''

'''n2=int(input())
list_2=[]
for i in range(1,11,1):
    list_2.append(n2*i)

print(list_2)
print(sum(list_2))'''

# linear search to find a given number in a list
'''list_1=list(map(int,input("enter list:").split()))
target=int(input())
for i in range(len(list_1)):
    if list_1[i]==target:
        print(i)
        break'''

#binary search
# only in sorted
'''list_2=[1,2,3,4,5,6,7,8]
print(list_2)
target=3
start=0
end=len(list_2)-1
index1=-1
while start<=end:
    middle= (start+end) //2
    if list_2[middle]==target:
        index1=middle
        break
    elif list_2[middle]<target:
        start=middle+1
    elif list_2[middle]>target:
        end=middle-1
print(index1)'''

#patterns problem

n=5
'''for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()

'''
'''for rows in range(n,0,-1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''

'''for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(rows,end=" ")
    print()'''


'''for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()'''

'''for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''
'''for rows in range(n,0,-1):
    for spaces in range(n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''
'''for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''

'''for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()

for rows in range(n,0,-1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()
'''
'''for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''n=
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
for rows in range(n,0,-1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()'''

n=6
'''for rows in range(n,0,-1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''


"""for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()"""

'''for rows in range(n,0,-1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()'''
'''for rows in range(n,0,-1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''for rows in range(1,n+1):
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''for rows in range(n,0,-1):
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=5
for rows in range(1,n+1):
    for spaces in range(n-rows):
        print(" ",end=" ")
    for cols in range(2*rows-1):
        print("*",end=" ")
    print()
    
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''


"""for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()
for rows in range(n-1,0,-1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()"""

"""for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()

for rows in range(n-1,0,-1):
    for spaces in range(n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()"""

'''for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()
for rows in range(n-1,0,-1):
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()'''
'''for rows in range(1,n+1):
    for spaces in range(n-rows):
        print(" ",end=" ")
    for cols in range(2*rows-1):
        print("*",end=" ")
    print()'''

n=5
'''for rows in range(1,n+1,1):
    for cols in range(1,n+1,1):
        if rows==1 or rows==n or cols==1 or cols==n:

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()'''
'''s=11
n=4
for rows in range(1,n+1,1):
    
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1,1):
        print(s,end=" ")
        s+=1
        
    print()'''
n=5
'''# Upper half
for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
    # Lower half
for i in range(n - 1, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

'''
for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()