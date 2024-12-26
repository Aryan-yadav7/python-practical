## practical 5- WAP to perform the following operations on a string. 

### a. find the frequency of a character in a string . 

string = "hello world to python"

character = input("enter a character ")

f=0

for i in string:

   if i ==character:
     f+=1
print("frequency of" , character ,'is', f)     




### b. replace a character by another character in a string .

string = "hello world to python"

print(string.replace ("e","i"))




### c. remove the first occurance os a character from a satring .

string = "hello world to python program"

print(string[3:len(string)])





### d. remove all the occurances of a character from a string

string = "hello world to python tutorial"

print(string[ :0])

print(string[ :2])




