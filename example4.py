#conditional statements
#if
#elif
#else
#nested if
''''if False:
    print("hello")
elif False:
    print("hi")
else:
    print("bye")
    '''
##if True:
##    print("outer region")
##    if False:
##        print("inner region")
##    elif True:
##        print("second inner")
##        if True:
##            print("hello")
##    else:
##        print("third inner")
##    
##else:
##    print("second outer")
'''
u="224G1A0210"
p="Manji@10"
user=input("Enter user ID: " )
pas=0
if u==user:
    pas=input("Enter Password: ")
    if p==pas:
        print("Login Successfully")
    else:
        print("Wrong password")
else:
    print("Invalid user ID")'''
    
##looping statements
##for
##while

'''a=input()
for i in a:
    print(i,end="-")'''


##n=int(input())
##for i in range(n):
##    print(n)

##n= int(input())
##for i in range(n):
##    print(i,end="-")


##n= int(input())
##for i in range(1,n+1):
##    print(i)


##l1=list(map(int,input("Enter numbers: ").split( )))


##l2=[1,2,3,5,6,7,8,9,0]
##for i in l2:
##    print(i*i)

##n = int(input())
##print("Even numbers are:",end=" ")
##for i in range(n+1):
##    if i%2==0:
##        print(i,end=" ")
    
##n = int(input())
##print("Odd numbers are:",end=" ")
##for i in range(n+1):
##    if i%2!=0:
##        print(i,end=" ")

##n = int(input())
##for i in range(1,n+1):
##    if i==5:
##        pass
##    print(i,end=" ")

##n = int(input())
##for i in range(1,n+1):
##    if i==5:
##        break
##    print(i,end=" ")
    
##n = int(input())
##for i in range(1,n+1):
##    if i==5:
##        continue
##    print(i,end=" ")


##n=int(input())
##print("odd numbers:",end=" ")
##for i in range(1,n+1,2):
##    print(i,end=" ")

##n=int(input())
##print("even numbers:",end=" ")
##for i in range(0,n+1,2):
##    print(i,end=" ")

### While


##n=int(input())
##i=1
##while i<=10:
##    print(n,"x",i,"=",n*i)
##    i+=1
          
##n=int(input())
##i=0
##while i<=10:
##    if i==0:
##        pass
##    print(n,"x",i,"=",n*i)
##    i+=1
    
 
##n=int(input())
##i=0
##while i<=10:
##    if i==7:
##        break
##    print(n,"x",i,"=",n*i)
##    i+=1

##
##n=int(input())
##i=0
##while i<=10:
##    if i==0:
##        continue
##    print(n,"x",i,"=",n*i)
##    i+=1

##n=int(input())
##i=1
##fact=1
##while i<=n:
##    fact*=i
##    i+=1
##print(fact)   
while True:
    n=int(input())
    i=n
    fact=1
    while i>1:
        fact*=i
        i-=1
    print(fact) 













    















