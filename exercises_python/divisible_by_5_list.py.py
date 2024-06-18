# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Expected Output:

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55


given_list = [10, 20, 33, 46, 55]
print('Given list is  [10, 20, 33, 46, 55]')
print('Numbers divisible by 5 in the list: ')

def divisible_five(list):
    for num in list:
        if num %5 == 0:
            print(num)


divisible_five(given_list)