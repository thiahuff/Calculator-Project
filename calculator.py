"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube, power, mod, )

# Replace this with your codede

result = None
while result == None:
    math_problem = input("write your equation here")
    tokens = math_problem.split(' ')

    

    math_operator = tokens[0]
    nums1 = float(tokens[1])
    if len(tokens) ==3:
        nums2 = float(tokens[2])

    if math_operator == "+":
        result = add (nums1,nums2)
    elif math_operator == "-":
        result = subtract (nums1,nums2)

    elif math_operator == "*":
        result = multiply (nums1,nums2)
 
    elif math_operator == "/":
        result = divide (nums1,nums2)

    elif math_operator == "**2":
        result = cube (nums1)
   
    elif math_operator == "**3":
        result = square (nums1)
     
    elif math_operator== "**":
        result = power (nums1,nums2)
  
    elif math_operator== '%':
        result = mod (nums1,nums2)


    print (result)