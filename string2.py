# to find the number vowels,consonants and spaces in a given string

'''s,c,v=0,0,0
str1=input().lower()
for i in str1:
    if i==" ":
        s+=1
    elif i in {"a","e","i","o","u"}:
        v+=1
    elif i in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        c+=1

print("vowels:",v)
print("consonents:",c)
print("space:",s)
'''

## WAP to find the ASCII value of the character

'''ch1=input()
print("ascii value:",ord(ch1))  # syntax: ord(character)'''

'''str1=input()
for i in str1:
    print(f"{i}={ord(i)}",sep="/n")
'''

# WAP to find the character from ASCII value

'''ascii_value=int(input())
print("character:",chr(ascii_value))'''
'''
for i in range(1000):
    print(i,":",chr(i))'''

# WAP to remove all the vowels in a string

'''str2=input()
res=""
for i in str2:
    if i.lower() not in {"a","e","i","o","u"}:
        res+=i
print(res)'''

# WAP to remove space from the string

'''str2=list(map(str,input().split()))
print(str2)
print(*str2,sep="")
print("".join(str2))'''
'''
str3=input()
str3=str3.split()
str3="".join(str3)
print(str3)'''

'''str3=input()
print(str3.replace(" ",""))'''


## WAP to remove all chars except alphabets

'''
str4=input()
res=""
for i in str4:
    if i.isalpha():
        res+=i
print(res)'''

#WAP to reverse a given string

str5=input()
print(str5[::-1])
for i in str5[::-1]:
    print(i,end="")
print()
for i in range(len(str5)-1,-1,-1):
    print(str5[i],end="")
print()

i=0                            # string does not assignment operation
j=len(str5)-1
while i<j:
    str5[i],str5[j]=str5[j],str5[i]
    i+=1
    j-=1
print(str5)    
