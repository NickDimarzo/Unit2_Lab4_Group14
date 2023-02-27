# Squaring a list
# Author: Dawson Gall

# List
nums = [2, 5, 6, 8, 11]
print("List of number trying square", nums)
# Computation
for i in nums:
    squares = [i**2 for i in nums]
print("List of numbers squared", squares)
