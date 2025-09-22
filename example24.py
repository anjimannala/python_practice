'''x=int(input())
p=int(input())
sum=1
for i in range(p):
    sum*=x
    print(sum)

print(sum)'''

x=int(input())
p=int(input())
sum=1
while p>0:
    if p%2==1:
        sum=sum*x
    x=x*x
    p=p//2
    print(1)
print(sum)


