#ex1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#ex2
number = 15
if number > 0:
  print("The number is positive")


#ex3
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#ex4
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#SHORT HAND IF
#ex5
a = 5
b = 2
if a > b: print("a is greater than b")

#ex6
a = 2
b = 330
print("A") if a > b else print("B")

#ex7
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#ex8
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)



