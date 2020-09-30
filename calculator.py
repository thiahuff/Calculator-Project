"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube, power, mod, )

print("Hey guys!")
# Replace this with your codede


while result == None:
    math_problem = input("")
    tokens = math_problem.split(' ')

    result = None

    math_operator = tokens[0]
    nums1 = tokens[1]
    if len(tokens) ==3:
        nums2 = tokens[2]

    if math_operator == "+":
        result = add (nums1,nums2)
        return result
    elif math_operator == "-":
        result = subtract (nums1,nums2)
        return result
    elif math_operator == "*":
        result = multiply (nums1,nums2)
        return result
    elif math_operator == "/":
        result = divide (nums1,nums2)
        return result
    elif math_operator == "**2":
        result = cube (nums1)
        return result
    elif math_operator == "**3":
        result = square (nums1)
        return result
    elif math_operator== "**":
        result = power (nums1,nums2)
        return result
    elif math_operator== '%':
        result = mod (nums1,nums2)
        return result

    print 
    




  
    print(output)