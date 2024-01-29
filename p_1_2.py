u=int(input("Enter no of stduents:"))
U=[]
for i in range(u):
  n=int(input("Enter roll no:"))
  U.append(n)
print(U)

A=[]
a=int(input("Enter no of students who play cricket:"))
for i in range(a):
  roll_a=int(input("Enter roll no:"))
  A.append(roll_a)
print("List of students who play cricket:-",A)

B=[]
b=int(input("Enter no of students who play badminton:"))
for i in range(b):
  roll_b=int(input("Enter roll no:"))
  B.append(roll_b)
print("List of students who play badminton:-",B)

C=[]
c=int(input("Enter no of students who play football:"))
for i in range(c):
  roll_c=int(input("Enter roll no:"))
  C.append(roll_c)
print("List of students who play cricket:-",C)

AIB=[]
for i in range(a):
  for j in range(b):
    if(A[i]==B[j]):
      AIB.append(A[i])
print("List of students who play cricket and badminton:-",AIB)

AB=[]
for i in range(a):
  AB.append(A[i])
  for j in range(b):
    flag=0
    if(A[i]==B[j]):
      flag=1
      break
  if(flag==0):
    AB.append(B[j])
print("List of students who play cricket or badminton:",AB)

x=len(AIB)
y=len(AB)
AOB=[]
for i in range(x):
  flag=0
  for j in range(y):
    if(AB[j]==AIB[i]):
      flag=1
      break
    if(flag==0):
      AOB.append(AB[j])
print("List of students who play cricket and badminton but not both:-",AOB)

UAB=[]
for i in range(u):
  flag=0
  for j in range(y):
    if(AB[j]==U[i]):
      flag=1
      break
  if(flag==0):
    UAB.append(U[i])
print("List of students who play neither cricket nor badminton:-",UAB)

ANC=[]
for i in range(a):
  A.append(A[i])
  for j in range(c):
    flag=0
    if(A[i]==C[j]):
      flag=1
      break
  if(flag==0):
    ANC.append(C[j])
print("List of students who plays cricket and football:-",ANC)

z=len(ANC)
AUC=[] #plays cricket and football but not badminton
for i in range(z):
  flag=0
  for j in range(b):
    if(ANC[i]==B[j]):
      flag=1
      break
  if(flag==0):
    AUC.append(ANC[i])
print("List of students who plays cricket and football but not badminton:-",AUC)