# Unit 2 Lab 4 ex 12
# Group 14
# Squares List

nums = [2, 5, 6, 8, 11]
new_nums = []


for number in nums:
    number = (number**2)
    new_nums.append(number)
    if number > 64:
        break

print(new_nums)




