# WAP that reads a two digit number N and
# check if any of the given conditions is satisfied

# 1, the number N is divisible by 9
# 2. one of the digits of the number N is equal to 9

# print lucky number if any of the given conditions is satisfied.otherwise,print unlucky number


'''
n = int(input())
n1=str(n).split()
if n%9==0 or 9 in n1:
    print("lucky number")
else:
    print("unlucky number")

''''''
n = input()
if int(n)%9==0 or int(n[0])==0 or int(n[1])==0 :
    print("lucky number")
else:
    print("unlucky number")

''''''
n = int(input())

if n%9==0 or 9 in str(n).split():
    print("lucky number")
else:
    print("unlucky number")
'''

# WAP that reads a distance D in KM and calculates the total score.

# for the first 40km 0-40 the score for each km is 2
# for the next 20km 41-60 the score for each km is 4
#  for the next 60km 61-120 the score for each km is 6
#  for the distance above 120km,the score for each km is 8
# apart from the above scores ,there is a bonous score of 50


'''
d=int(input())
score=0
if d>=0 and d<=40:
    score=d*2+50
elif d>=41 and d<=60:
    score=40*2 +(d-40)*4+50   # score=80+50+(d-40)*4
elif d>=61 and d<=120:
    score=40*2 +20*4+(d-40-20)*6+50  # score=80+80+50+(d-40-20)*6
elif d>120:
    score=40*2+20*4+60*6+(d-40-20-60)*8+50  # score=80+80+360+5+(d-40-20-60)*8
print(score)
'''

'''# WAP to no of notes of 500,50,5,1 for the given amount
a=int(input())
if a>5:
    ones=a
elif 4< a <=5:

    '''

## WAP that reads two numbers x and N and prints the product of n numbers after x
# the first line of input contains an integre representing x
#the second line of input contains an integer represnting n
# output   the op should contains a single line containing an integers obtained by multipling the n numbers after x 
'''

x=int(input())
n=int(input())
pro=1
n1=1
while n1<=n:
    x+=1
    pro*=x
    n1+=1
pro=1
for i in range(x+1,x+n+1):
    pro*=i
print(pro)'''

'''
s="aaaabbbbccc"
res={}
for i in s:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
for i,c in res.items():
    print(f"{i}{c}",end="")'''


m=int(input())
n=int(input())

def isprime(num):
    if num==0 or num<0 or num==1:
            return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True


for i in range(m,n+1):
    if isprime(i):
        print(i,end=" ")
