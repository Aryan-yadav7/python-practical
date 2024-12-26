## practical 11 - consider a tuple t1 =(1,4,6,3,2,8,5,10,9,7,6). WAP to perform the following.

### (a.)  print half the values of the tuple in one line and other half in the other next line.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

half_value=len(t1)//2

first_half = t1[ :half_value]

print("first_half" ,first_half )

second_half = t1[half_value: ]

print("second_half" ,second_half )   

![Screenshot 2024-11-07 153337](https://github.com/user-attachments/assets/ec1f42c5-a0cd-45bf-8ddc-6f698f086fc3)

### (b.) Print another tuple whose values are even numbers in a given tuple.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

even_number = tuple(filter(lambda x: x%2==0, t1))

print("tuple with even number ", even_number )

![Screenshot 2024-11-07 154105](https://github.com/user-attachments/assets/9047ffe3-d839-4ad8-a6d2-101b85dd11f8)


### (c.) Concatenate a tuple t2 =(12,15,11) with t1.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

t2 =(12,15,11)

concatenation= (t1 ,t2)

print("tuple with concatenation  ", concatenation )

![Screenshot 2024-11-07 154606](https://github.com/user-attachments/assets/96394980-9de9-4dc6-8954-ecdb623c90f3)

 

### (d.) return Maximum and minimum value from this given tuple.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

print("maximum value in t1 is ", max(t1))

print("minimum value in t1 is ", min(t1))
