#linear_search
l = int(input("Enter no of students prsent for a program:"))
l1 = []
for i in range(l):
  roll = int(input("Enter roll no of students:"))
  l1.append(roll)
print("Students who attended training session", l1)
a = int(input("Enter the roll no you want to check:"))
for i in range(l):
  flag = 0
  if (a == l1[i]):
    flag = 1
    break
if (flag == 1):
  print("Student is present")
else:
  print("Student is absent")

#fibonacci_search
fib1=1
fib2=0
fib=fib1+fib2
while(fib<1):
  fib1=fib
  fib2=fib1
  fib=fib1+fib2
i=0
offset=-1
flag=0
while(fib>=1):
  i=min(offset+fib2,l-1)
  if(a==l1[i]):
    flag=1
    break
  elif(a>l1[i]):
    fib=fib1
    fib1=fib2
    fib2=fib-fib1
  elif(a<l1[i]):
    fib=fib2
    fib1=fib1-fib2
    fib2=fib-fib1
if(flag==1):
  print("Student is present")
else:
  print("Student is absent")

