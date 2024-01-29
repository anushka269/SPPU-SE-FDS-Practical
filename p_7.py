#for sentinel search:   
l=int(input("no of students present for traning session:"))
l1=[]
for i in range (l):
    roll=int(input("roll no of students:"))
    l1.append(roll)
print("students who attended training session:",l1)
a=int(input("Enter the roll no you want to check:") )
l2=[]    
for i in range(l):
    l2.append(l1[i])
l2.append(a)

j=0
while(j<l):

    if(a==l2[j]):
        break
    else:   
        j=j+1 

if(j<l):
    print("location of roll no",j) 
    print("student is present")
else:
    print("student is absent") 

#binary search
l1.sort()
low=0
high=l-1
flag=0
while(low<=high):
    mid=(low+high)//2
    if (l1[mid]==a):
        flag=1
        break
    elif(a<l1[mid]):
        high=mid-1
    else:
        low=mid+1
if flag==1:
    print("student is present")
else:
    print("student is absent") 