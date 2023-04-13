def sum_of_digits(x):
    temp_int = 0
    for index in x:
        temp_int += int(index)
    return temp_int


def largest_number(value1, value2, value3):
    if value1 > value2 and value1 > value3:
        return value1
    elif value2 > value3:
        return value2
    else:
        return value3


def count_even_odd(user_even_odd):
    even_count = 0
    for index in user_even_odd:
        if int(index) % 2 == 0:
            even_count += 1
    return even_count


# 1 Compute the sum of digits in all numbers from 1 to n
user_input = input('Enter number: ')
print(f'the sum of digits you\'ve input is {sum_of_digits(user_input)}')


# 2 Find the max number from 3 values
first_value = int(input('\nEnter first number: '))
second_value = int(input('Enter second number: '))
third_value = int(input('Enter third number: '))

print(f'The largest number you input is {largest_number(first_value, second_value, third_value)}')


# 3 Count odd and even numbers
user_number = input('\nEnter number: ')
even_amount = count_even_odd(user_number)
print(f'There are {even_amount} even numbers and {len(user_number) - even_amount} odd numbers in {user_number}')
