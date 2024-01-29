r1=int(input("Enter number of rows:"))
c1=int(input("ENter no of columns:"))
m1=[]
for i in range(r1):
  t1=[]
  for j in range(c1):
    t1.append(int(input("Enter values:")))
  m1.append(t1)
print("Matrix A =")
for rm1 in m1:
  print(rm1)

r2=int(input("Enter no of rows:"))
c2=int(input("Enter no of columns:"))
m2=[]
for i in range(r2):
  t2=[]
  for j in range(c2):
    t2.append(int(input("Enter values:")))
  m2.append(t2)
print("Matrix B=")
for rm2 in m2:
  print(rm2)

m3=[]
for i in range(r1):
  t3=[]
  for j in range(c1):
    t3.append(0)
  m3.append(t3)
for i in range(r2):
  for j in range (c2):
    m3[i][j]=m1[i][j]+m2[i][j]
print("Addition of matrix A and B=")
for rm3 in m3:
  print(rm3)

ms=[]
for i in range(r1):
  t4=[]
  for j in range(c1):
    t4.append(0)
  ms.append(t4)
for i in range(r2):
  for j in range(c2):
    ms[i][j]=m1[i][j]-m2[i][j]
print("Substraction of matrix A and B = ")
for rms in ms:
  print(rms)

if(c1==r2):
  mm=[]
  for i in range(r1):
    tm=[]
    for j in range(c2):
      tm.append(0)
    mm.append(tm)
  for i in range(r1):
    for j in range(c2):
      mm[i][j]=0
      for k in range(c2):
        mm[i][j]+=m1[i][j]*m2[i][j]
print("Multiplication of matrix A and B = ")
for rmm in mm:
  print(rmm)

mt=[]
for i in range(r1):
  tt=[]
  for j in range(c1):
    tt.append(0)
  mt.append(tt)
for i in range(r1):
  for j in range(c1):
    mt[i][j]=m1[j][i]
print("Transpose of matrix A = ")
for rmt in mt:
  print(rmt)