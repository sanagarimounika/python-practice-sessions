# Operators
# are symbols that perform operations on variables and values 

# Types 
# Arthematic operators
# Addition 
x = 10
y = 5
print(x + y) # without interpolation
print(x % y)
print("---------------")
print(f"sum of {x} and {y} is {x + y}") # with interpolation
print(f"Difference of {x} and {y} is {x - y}")
print(f"Product of {x} and {y} is {x * y}")
print(f"Division of {x} and {y} is {x / y}")
print(f"Modulus of {x} and {y} is {x % y}")

# floor division
print(f"Normal division of {x} and {y} is {x / y}")  # 2.0 Always returns a float (decimal value), even if the result is a whole number.
print(f"Floor division of {x} and {y} is {x // y}")  # 2 Performs division and then rounds down to the nearest whole integer.

# Exponentiation
print(f"Exponentiation of {x} and {y} is {x ** y}")                          

print("========================================================================")

# COMPARISON OPERATORS
a = 10
b = 20
print(a==b) # equal to
print(a!=b) # not equal to
print(a>b)  # greater
print(a<b)  # less then
print(a>=b) # greater or equal
print(a<=b) # less or equal
print("========================================================================")

# LOGICAL OPERATORS
x = 10
y = 5
a = 15
b = 20
# AND - if both are true
result_and = x > y and a < b
print(result_and)
result_and = x < y and a > b
print(result_and)
print("---------------------")

# OR - true if any true
result_or =  x > y or a < b
print(result_or)
result_or = x < y or a > b
print(result_or)
result_or = x < y or a < b
print(result_or)

print("---------------------")

# NOT - Reverses boolean
result_not = x < y or a < b # F or F > F
print(result_not)           # False
print(not result_not)       # True     
print("++++++++++++++++++++++")
result_and = x > y and a < b # T and T > T
print(result_not)            # True
print(not result_not)        # False

print("=====================================================================================")

# MEMBERSHIP OPERATORS
