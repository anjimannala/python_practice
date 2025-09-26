## exception handling

'''try:
    num=input()
    num=int(num)
    res=100//num
    print(num,res)
    #print(num+"ghdj")
    #print(num3)
    list1=["ghjd"]
    #print(list1[18])
### when we give different type of input 
except ValueError:
    print("invalid input")

### error occured when ooperations perfomed on different types of data
except TypeError:
    print("can't perform  operation of different types")

### erroro when a num is divided by zero
except ZeroDivisionError:
    print("can't divided with zero")

### using of not defined variables or functions
except NameError:
    print("var or function not defined")

### when index is out of reach
except IndexError:
    print("index is out of range")

### general handling when dont know error 
except Exception as e:
    print("error:",e)

### executes when no exceptions
else:
    print("no error go ahead")
### prints at the end
finally:
    print("end")'''

## wap to find the roots of the quadratic equation

'''
def roots(a,b,c):
    if a==0:
        return print("Invalid input a not equal to 0")
    else:
        d=b*b - 4*a*c
        if d>0:
            print("roots are real and different")
            root1= ((-b)+(d**0.5))/2*a
            root2= ((-b)-(d**0.5))/2*a
            print("root1=",root1," and root2=",root2)
        elif d==0:
            print("roots are real and equal")
            print("root1 =",(-b)/2*a,"and root2 =",(-b)/2*a)

        else:
            print("roots are complex and conjugate")
            root1= ((-b)+(d**0.5))/2*a
            root2= ((-b)-(d**0.5))/2*a
            print("root1=",root1," and root2=",root2)

print("enter the co efficients of the quadratic equation ax^2+bx+c")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
roots(a,b,c)'''

### problems on number systems
# decimal to binary,octal,hexadecimal using standard methods
'''print(bin(12))

print(oct(12))

print(hex(12))'''

## decimal to binary,octal,hexadecimal brutforce
# decimal to binary

'''dec=int(input())
print(bin(dec)[2::])
res=""
while dec>0:
    rem=dec%2
    dec=dec//2
    res+=str(rem)
print(int(res[::-1]))'''

## decimal to octal
'''dec=int(input())
print(oct(dec)[2::])
res=""
while dec>0:
    rem=dec%8
    dec=dec//8
    res+=str(rem)
print(int(res[::-1]))'''

## decimal to hexadecimal

'''dec=int(input())
print(hex(dec)[2::])
hexchars="0123456789abcdef"
res=""
while dec>0:
    rem=dec%16
    dec=dec//16
    res+=hexchars[rem]
print(res[::-1])'''

## binary,octal,hexadecimal to decimal brutforce
## b to d
'''b=str(input())
d=0
p=0
for i in b[::-1]:
    d+=int(i)*(2**p)
    p+=1
print(d)
print(0b0111101010100010)'''

# o to d

'''o=str(input())
d=0
p=0
for i in o[::-1]:
    d+=int(i)*(8**p)
    p+=1
print(d)
print(0o74123665)'''

## h to d

'''h=input()
hexchars="0123456789abcdef"
d=0
p=0
for i in h[::-1]:
    d+=hexchars.index(i) * (16**p)
    p+=1
print(d)
print(0x164b6ae)'''

# WAP to add the two fractional numbers

def gcd(num1,num2):
    while num2:
        num1,num2=num2,num1%num2
    return num1

def lcm(num1,num2):
    res=(num1*num2)//gcd(num1,num2)
    return res

def add_2fr(num1,den1,num2,den2):
    den3=lcm(den1,den2)
    #print("den3=",den3)
    num1=num1 * (den3//den1)
    #print("num1:",num1)
    num2=num2 * (den3//den2)
    #print("num2:",num2)
    num3=num1+num2
    #print("num3:",num3)
    num3,den3=num3//gcd(num3,den3),den3//gcd(num3,den3)
    #print("num3:",num3)
    #print("den3:",den3)
    return print(f"result: {num3}/{den3}" if den3!=1 else f"result: {num3}")

def addition_two_fractions():
    num1,den1=map(int,input("f1:").split("/"))
    num2,den2=map(int,input("f2:").split("/"))
    try:
        add_2fr(num1,den1,num2,den2)
    except ZeroDivisionError:
        print("invalid Input")
#addition_two_fractions()

# binary to octal conversion
def bin_dec(b):
    d=0
    p=0
    for i in b[::-1]:
        d+=int(i)*(2**p)
        p+=1
    return d
def dec_oct(dec):
    res=""
    while dec>0:
        rem=dec%8
        dec=dec//8
        res+=str(rem)
    return int(res[::-1])
def dec_hex(dec):
    hexchars="0123456789abcdef"
    res=""
    while dec>0:
        rem=dec%16
        dec=dec//16
        res+=hexchars[rem]
    return str(res[::-1])
'''num=input()
res=dec_oct(bin_dec(num))
print(res)'''
#print(oct(0b1010)[2::])

## binary to hex
'''num=input()
res=dec_hex(bin_dec(num))
print(res)
print(hex(0b11110101001)[2::])'''

# WAP to convert the digits/numbers into words

num1=int(input())
ones=["","one","two","three","four","five","six","seven","eight","nine"]
teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
res=""
if num1>=1000:
    res+=ones[num1//1000]+" thousand"+" "
    num1=num1%1000
if num1>=100:
    res+=ones[num1//100]+" hundred"+" "
    num1=num1%100
if num1>=20:
    res+=tens[num1//10]+" "
    num1=num1%10
elif num1>=10:
    res+=teens[num1-10]+" "
    num1=num1%10
if num1>0:
    res+=ones[num1]
print(res)