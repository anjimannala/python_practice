''''n=int(input())
for rows in range(1,n+1):
    for cols in range(rows):
        print("*",end=" ")
    print()

n=int(input())

for rows in range(1,n+1):
    for cols in range(n):
        
        print(n,end=" ")
    print()
    n-=1

n=int(input())
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()

n=int(input())
for rows in range(1,n+1):
    for cols in range(n):
        print(n-cols,end=" ")
        
    print()
    n-=1
'''
