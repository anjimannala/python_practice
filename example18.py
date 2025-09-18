'''list1=[4,6,5,3,2]
target=6
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]==target:
            print(list1[i],list1[j])
            break
'''
# wrong did not pass test cases

'''list1=[4,6,5,3,2]
target=4
for i in list1:
    req=target-i
    if req in list1:
        print(i,req)
        break'''
# set oe two elements sum
'''

list1=[-1,3,2,4,12]
target=9
uniq=set()
for i in list1:
    req=target-i
    if req in uniq:
        print(i,req)
        break
    uniq.add(i)
'''
# to print missing number in a list


'''list2=[1,2,3,4,6,7]
for i in range(len(list2)-1):
    if list2[i]+1!=list2[i+1]:
        print(list2[i]+1)
        break
'''        

# given n-1 integers in the range 1 to n with no duplicates,find the missing no
'''list1=[1,2,3,5,6]
sum1=sum(list1)
sum2=len(list1)*(len(list1)+1)//2
print(sum2-sum1)'''

# sum of first n natural numbers

'''n=5
sum1=n*(n+1) // 2
print(sum1)'''
'''
list1=[1,2,3,4,5]
k=2
n=len(list1)-1
temp=0
for i in range(k):
    temp=list1[0]
    for j in range(n):
        list1[j]=list1[j+1]
    list1[n]=temp
print(list1)


list1=[1,2,3,4,5]
k=2
n=len(list1)-1
temp=0
for i in range(k):
    temp=list1[n]
    for j in range(n,0,-1):
        list1[j]=list1[j-1]
    list1[0]=temp
print(list1)'''