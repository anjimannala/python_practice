'''list1=[2,3,-1,8,4]
lsum=0
rsum=0
for i in range(len(list1)):
    lsum=sum(list1[0:i:])
    rsum=sum(list1[-1:i:-1])
    print(lsum,rsum)
    if lsum==rsum:
        print(i)
        print(lsum)
        print(rsum)
        break'''
'''Problem Statement: Finding Equilibrium index in an array

Given a 0-indexed integer array nums, find the leftmost equilibrium Index.

An equilibrium Index is an index at which sum of elements on its left is equal to the sum of element on its right. That is, nums[0] + nums[1] + ... + nums[equilibriumIndex-1] == nums[equilibriumIndex+1] + nums[equilibriumIndex+2] + ... + nums[nums.length-1]. If equilibriumIndex == 0, the left side sum is considered to be 0. Similarly, if equilibriumIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost equilibrium Index that satisfies the condition, or -1 if there is no such index.'''
'''
list1=[2,3,-1,8,4]
list1=[1,-1,4]
list1=[1, 2, 3, 4, 6]
list1=[1, 7, 3, 6, 5, 6]
list1=[-7, 1, 5, 2, -4, 3, 0]
lsum=0
rsum=0
for i in range(len(list1)):
    lsum=sum(list1[0:i:])
    rsum=sum(list1[-1:i:-1])
    if lsum==rsum:
        print("the mid index is",i)
        break
else:
    print("no mid index found")

'''


'''Problem Statement: Given an array of N integers, the task is to replace each element of the array by its rank in the array.

Examples:

Example 1:
Input: 20 15 26 2 98 6
Output: 4 3 5 1 6 2
Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1,rank of 6 is 2,rank of 15 is 3 and so…'''


'''list2=[20,15,26,2,98,6]
for i in list2:
    set2=set()
    for j in list2:
        if j<i:
            set2.add(j)
    rank=len(set2)+1
    print(rank,end=" ")'''


#ip= 5
#op= 122333444455555

'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
'''
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

'''n=int(input())
for i in range(2,n+1):
    if isprime(i):
        print(str(i)*i,end="")'''

'''
amt=int(input())
print("500 notes=",int(amt//500))
print("50 notes=",int((amt%500)//50))
print("10 notes=",int(((amt%500)%50)//10))
print("1 notes=",int(((amt%500)%50)%10))
'''

# ip=8
# op=4
# factor that is less than num

'''
n=int(input())
flc=0
for i in range(1,n):
    if n%i==0:
        flc=i
if flc==0:
    print("no factors")
else:print(flc)
'''


str1=input().split()
for i in str1:
    print(i[::-1],end="")
    print(end=" ")