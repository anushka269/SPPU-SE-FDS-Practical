#bubble sort

n=int(input("Enter no of students:"))
A=[]
for i in range(n):
  a=float(input("Enter the percentage of student:"))
  A.append(a)
print("list:",A)

def bubble():
  for i in range(n):
    flag=0
    for j in range(0,n-i-1):
      if(A[j]>A[j+1]):
        b=A[j]
        A[j]=A[j+1]
        A[j+1]=b
        flag=1
    if(flag==0):
      break
bubble()
print("list of percentage of student:",A)
    
#selection sort:

index=0
for i in range (n-1):
    min=A[i]
    minindex=1
    for j in range(i+1, n):
        if min>A[j]:
           min=A[j]
           minindex=j
           A[i],A[minindex]=A[minindex],A[i]         
print("Sorted List by selection sort=",A)

