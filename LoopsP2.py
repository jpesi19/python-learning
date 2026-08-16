#Example 1: For Loop Basics
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Example 2: For Loop a String
for x in "banana":
  print(x)

#Example 3: For Loop range() function
for y in range(6):
  print(y)

#Example 4: for loop with an increment set at the end of the range() function
 
for z in range(2,25,4):
  print(z)

#Example 5:
for x in range(5):
  print(x)
else:
  print("Finally Finished!")

#Example 6: tHE else will not work if the loop is broken by the break statement
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally Finished X2 ")

#Example 7: Nested For loops dude
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x,y)