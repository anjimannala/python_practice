## WAP to check the string is palindrome or not
# brute force
'''str1=input().lower()
res=True
for i in range((len(str1)//2)):
    if str1[i]!=str1[len(str1)-1-i]:
        res=False
        break
print("yes" if res else "no")'''

# optimized
'''str1=input()
print("yes" if str1.lower()==str1[::-1].lower() else "no")
'''
## recursive approach

'''
def ispalindrome(s1,i):
    if i>=len(s1)//2:
        return True
    if s1[i]!=s1[len(s1)-1-i]:
        return False
    return ispalindrome(s1,i+1)
    

str1=input().lower()
if ispalindrome(str1,0):print("yes")
else:print("no")'''