#longest word in a string

str=input("Enter the string:")
s=str.split()
m=0
for i in range(len(s)):
  if(m<len(s[i])):
    m=len(s[i])
    c=i
print("Longest word is:",s[c])

#check palindrome or not
str1=input("Enter the string:")
s1=str1[::-1]
if(s1==str1):
  print("Palindrome")
else:
  print("Not Palindrome")

#occurence of each word in a string
str4=input("Enter the string:")
count=dict()
words=str4.split()
for word in words:
  if(word in count):
    count[word]+=1
  else:
    count[word]=1
print(count)
    
#occurence of particular char in string
str5=input("Enter the string:")
s5=input("Enter the character:")
count=0
for i in range(len(str5)):
  if(s5==str5[i]):
    count+=1
print("Occurence of",s5,"is",count)

#substring
str6=input("Enter the string:")
sub=input("Enter the substring:")
found=0
for i in range(len(str6)):
  if(str6[i:i+len(sub)]==sub):
    found=1
    break
if(found==1):
  print("String found")
else:
  print("not found")