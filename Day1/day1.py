# import math

# # ### Day 1: Python Basics
# # Start by installing Python and a text editor. Learn the basics of Python, such as: 
# #  variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

# # #### Exercise
# # Simple Python Calculator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 
# # ADDITION
# x = 15
# y = 19
# print(x+y)

# # SUBTRACTION
# x = 98
# y = 35
# print(x-y)

# # DELETION
# x = [15,23,88,90]
# del x[2]
# print (x)

# # DIVISION
# x = 55
# y = 5
# print(x // y)

# # POWER
# x = pow (5, 4)
# print(x)

# # SQUARE ROOT
# x = math.sqrt(144)
# print(x)
def Calculator():
     numOne = int(input("Enter Num 1: "))
     numTwo = int(input("Enter Num 2: "))

     operand = int(input("Enter the Operand '\n' 1:Add '\n' 2:Subtract '\n' 3:Multiply,'\n' 4:Divide: '\n' 5:Deletion,'\n' 6:Power,'\n' 7:SquareRoot,'\n' "))
     if operand == 1:
          return numOne + numTwo
     elif  operand == 2:
          return numOne - numTwo
     elif  operand == 3:
          return numOne * numTwo
     elif  operand == 4:
          return numOne // numTwo
     elif  operand == 6:
          return numOne ** numTwo
     elif operand == 7:
          return numOne **0.5 and numTwo ** 0.5
         

if __name__ == "__main__":
     result = Calculator()
     print(result)