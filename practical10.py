
## practical 10 - Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are the cubes of the keys .

def cubes():
 
 dict={}

 for i in range (1,9):
 
   dict[i] = i**3

 print(dict)

cubes()
