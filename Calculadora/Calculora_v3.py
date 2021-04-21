import math

print(15 * '#', 'PYTHON CALCULATOR', 15 * '#')
print('Select the number for the operation you want?\n')
print('1 - SUM')
print('2 - SUBTRACTION')
print('3 - MULTIPLICATION')
print('4 - DIVISION')
print('5 - DIVISION(with module)')
print('6 - ENTIRE PART OF THE DIVISION')
print('7 - SQUARE ROOT\n')


def sum_option(x, y):
    return x + y


def sub_option(x, y):
    return x - y


def mult_option(x, y):
    return x * y


def div_option(x, y):
    return x / y


def module_option(x, y):
    return x % y


def entire_part(x, y):
    return x // y


def square_root(x):
    return math.sqrt(x)


option = int(input('Select one option (1, 2, 3, 4, 5, 6, 7): '))


if 0 < option < 6:
    first_number = float(input('Type it the first number: '))
    second_number = float(input('Type it the second number: '))
else:
    one_number = float(input('Type it one number: '))


if option == 1:
    print('OPERATION OF SUM:')
    print(f'{first_number} + {second_number} = {sum_option(first_number, second_number)}')
elif option == 2:
    print('OPERATION OF SUBTRACTION:')
    print(f'{first_number} - {second_number} = {sub_option(first_number, second_number)}')
elif option == 3:
    print('OPERATION OF MULTIPLICATION:')
    print(f'{first_number} * {second_number} = {mult_option(first_number, second_number)}')
elif option == 4:
    print('OPERATION OF DIVISION')
    print(f'{first_number} / {second_number} = {div_option(first_number, second_number)}')
elif option == 5:
    print('OPERATION OF DIVISION WITH MODULE:')
    print(f'{first_number} / {second_number} = {div_option(first_number, second_number)}')
    print(f'{first_number} % {second_number} = {module_option(first_number, second_number)}')
elif option == 6:
    print('OPERATION OF ENTIRE PART OF THE DIVISION:')
    print(f'{first_number} // {second_number} = {entire_part(first_number, second_number)}')
elif option == 7:
    print(8*'>', 'OPERATION OF SQUARE ROOT:')
    print(8*'>', f'√{one_number} = {square_root(one_number)}')
else:
    print(20 * '*')
    print('ERRO, REBOOT THE CODE')
    print(20 * '*')
