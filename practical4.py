# WAP that accepts a character and performs the following: 
# a) print if it's a letter, digit, or special character
# b) if it's a letter, check if it's uppercase or lowercase
# c) if it's a digit, print its name in text

charac = input("Enter the data: ")

if charac >= 'A' and charac <= 'Z':
    
   print(charac, "is an Uppercase Letter")

elif charac >= 'a' and charac <= 'z':
    
   print(charac, "is a Lowercase Letter")

elif charac >= '0' and charac <= '9':
    
   print(charac, "is a Numeric Digit")
   n = int(charac)
   
   dict= {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
    
   print(dict[n])

else:

   print(charac, "is a Special Character")   
