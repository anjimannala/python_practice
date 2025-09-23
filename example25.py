'''arr=[1,2,3,2,1]
arr1=[]
temp=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        arr1.append(arr[i:j+1])
for i in arr1:
    print(i)'''
'''arr=[1,2,3,2,1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        print(*arr[i:j+1])
   ''' 

'''arr=list(map(int,input().split()))
n=len(arr)    
for length in range(1,n+1):
    for j in range(n-length+1):
        sub_arr=arr[j:j+length]
        if sub_arr==sub_arr[::-1]:
            print(*sub_arr)
'''
'''rows=int(input())
cols=int(input())
main=[]
for i in range(rows):
    sub=[]
    for j in range(cols):
        sub.append(int(input()))
    main.append(sub)
    print()
print(main)

for i in range(rows):
    for j in range(cols):
        print(main[i][j],end=" ")
    print()'''

'''rows=int(input())
cols=int(input())
main=[]
for i in range(rows):
    main.append(list(map(int,input().split(" "))))
for i in range(rows):
    for j in range(cols):
        print(main[i][j],end=" ")
for j in range(cols):
    for i in range(rows):
        print(main[i][j],end=" ")'''
rows=3
cols=3
main=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(rows):
    for j in range(cols):
        print(main[i][j],end=" ")
    print()

top=0
bottom=rows-1
left=0
right=cols-1
while top<=bottom and left<=right:
    for i in range(left,right+1):
        print(main[top][i],end=" ")
    top+=1
    for i in range(top,bottom+1):
        print(main[i][right],end=" ")
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            print(main[bottom][i],end=" ")
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            print(main[i][left],end=" ")
        left+=1
