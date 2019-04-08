import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
num1=int(input("Enter number of passwords needed \n"))
num2=int(input("Enter the lengths of passwords \n"))
for y in range(num1):
  password =  "".join(choice(characters) for x in range(num2))
  print (password)
