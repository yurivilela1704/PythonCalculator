print(15 * '#', 'PYTHON CALCULATOR', 15 * '#')
print(' ')
print('Select the number for the operation you want?')
print(' ')
print('1 - SUM')
print('2 - SUBTRACTION')
print('3 - MULTIPLICATION')
print('4 - DIVISION')
print(' ')


option = int(input('Select one option (1, 2, 3, 4): '))
first_number = float(input('Type it the first number: '))
second_number = float(input('Type it the second number: '))


if option == 1:
    print('OPERATION OF SUM')
    sum_option = first_number + second_number
    print(format(f'{first_number} + {second_number} = {sum_option}'))
elif option == 2:
    print('OPERATION OF SUBTRACTION')
    sub_option = first_number - second_number
    print(format(f'{first_number} - {second_number} = {sub_option}'))
elif option == 3:
    print('OPERATION OF MULTIPLICATION')
    mult_option = first_number * second_number
    print(format(f'{first_number} * {second_number} = {mult_option}'))
elif option == 4:
    print('OPERATION OF DIVISION')
    div_option = first_number / second_number
    print(format(f'{first_number} * {second_number} = {div_option}'))
else:
    print(20*'*')
    print('ERRO, REBOOT THE CODE')
    print(20 * '*')
