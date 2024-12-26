## practical 3 - WAP to create a pyramid of the character '*' and a reverse pyramid.



def print_pyramid(n):
   
   for i in range(n):
     
     print(' ' * (n - i - 1), end='')
     
     print('*' * (2 * i + 1))

#Number of rows for the pyramid
rows = 5

print("Pyramid:")

print_pyramid(rows)


def print_reverse_pyramid(n):
   
   for i in range(n, 0, -1):
    
     print(' ' * (n - i), end='')
    
     print('*' * (2 * i - 1))

#Number of rows for the reverse pyramid
rows = 5

print("\nReverse Pyramid:")

print_reverse_pyramid(rows)
