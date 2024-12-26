## practical 12- WAP to accept a name from a user. Raisen and handle appropriate exception(s) if the text entered by the user contains digits and /or special characters . 

name =input("enter a name ")

try:
   
    if name.isalpha():
       
       print(" This is correct name ")

    else:
      
       raise Exception(" There is name error ")

except Exception as e:
   
    print(e)
