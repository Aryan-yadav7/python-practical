## practical 8 - WAP  to create a list of only the even integers appearing in the list (may have elements of other types ) using for loop and list comprehension.

def cubes():
  
  newlist =[]
  
  number = [1,3,5,2,7,4,"five"]

  for i in number:
  
   if type(i)==int:
   
     if i%2 ==0:
      
       newlist.append(i**3)
  
  print(newlist)

cubes()
