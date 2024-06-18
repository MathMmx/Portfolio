# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# Expected Output:

# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def list_first_last(list):
        if list[0] == list[-1]:
            print('The result is True')
        else:
            print('The result is False')

print('Given list: [10, 20, 30, 40, 10] ')
list_first_last(numbers_x)
print('Given list: [75, 65, 35, 75, 30] ')
list_first_last(numbers_y)