## practical 5 - WAP to swap the first n characters of two strings .

str1 =input("enter first string ")

str2 =input("enter second string ")

n1 =int(input("enter no of characters which is to be swap: "))

n=str1[ :n1]

m=str2[ :n1]

if n1 <= min(len(str1),len(str2)):
  
  print(str1.replace(n,m))

else:
  
  print(str2.replace(n,m))
