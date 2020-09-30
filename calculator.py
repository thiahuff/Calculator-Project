"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube, power, mod, )

print("Hey guys!")
# Replace this with your codede
while result == None:
    math_problem = input("")
    tokens = math_problem.split(' ')

    math_operator = tokens[0]
    nums1 = tokens[1]
    if len(tokens) ==3:
        nums2 = tokens[2]

    if math_operator == "+":
        return add (nums1,nums2)
    elif math_operator == "-":
        return subtract (nums1.nums2)
    elif math_operator == "*":
        return multiply (nums1,nums2)
    elif math_operator == "/":
        return divide (nums1,nums2)
    elif math_operator == "**2":
        return cube (nums1)
    elif math_operator == "**3":
        return square (nums1)
    elif math_operator== "**":
        return power (nums1,nums2)
    elif math_operator== '%':
        return mod (nums1,nums2)
    




  
    print(output)