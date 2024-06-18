# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:

# result list: [25, 35, 40, 60, 90]


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print(len(list1))
print(len(list2))
def test_list(list1, list2):
    new_list = []

    for num in list1:
        if num %2 != 0:
            new_list.append(num)
    
    for num in list2:
        if num %2 == 0:
            new_list.append(num)
    return new_list

print(test_list(list1, list2))