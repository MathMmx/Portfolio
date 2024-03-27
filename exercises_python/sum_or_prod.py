       # Exercise 1: Calculate the multiplication and sum of two numbers
    # Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

    # Given 1:

    # number1 = 20
    # number2 = 30
    # Expected Output:

    # The result is 600
    # Given 2:

    # number1 = 40
    # number2 = 30
    # Expected Output:

    # The result is 70

number1 = int(input('Insert number 1: ' ))
number2 = int(input ('Insert number 2: ' ))


if number1 * number2 > 1000:
        print('The result is ') 
        print(number1 + number2)
else: 
        print('The result is ')
        print(number1 * number2)

    
#solução do site
# def multiplication_or_sum(num1, num2):
#     # calculate product of two number
#     product = num1 * num2
#     # check if product is less then 1000
#     if product <= 1000:
#         return product
#     else:
#         # product is greater than 1000 calculate sum
#         return num1 + num2

# # first condition
# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# # Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)