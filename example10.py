'''l1=[2,95,3,46,7,12]
la=0
for i in l1:
    if i>la:
        la=i
print(la)
    
l1.sort()
print(l1)
print(l1[-1])
print(l1[0])
print(l1[1])
print(l1[-2])
l1.sort(reverse=True)
print(l1)'''
l2=[1,6,3,78,3]
print(l2[-1::-1])
def rs():
    s=0
    e=len(l2)-1
    while s<=e:
        l2[s],l2[e]==l2[e],l2[s]
        s+=1
        e-=1
    print(l2)

rs()