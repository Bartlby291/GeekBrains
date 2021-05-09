def Sum_max_numb(x, y, z):
    if y > z and x > z:
        return x + y
    elif y > x and z > x:
        return y + z
    elif x > y and z > y:
        return x + z
    elif x == y == z:
        return x + y
    elif x == y > z:
        return x + y
    elif x == z > y:
        return x + z
    else:
        return z + y
Number_1 = None
while Number_1 == None:
    try:
        Number_1 = float(input('Введите число >>> '))
    except ValueError:
        print('Вы вели не число, попробуйте еще раз')
Number_2 = None
while Number_2 == None:
    try:
        Number_2 = float(input('Введите число >>> '))
    except ValueError:
        print('Вы вели не число, попробуйте еще раз')
Number_3 = None
while Number_3 == None:
    try:
        Number_3 = float(input('Введите число >>> '))
    except ValueError:
        print('Вы вели не число, попробуйте еще раз')
print(f'Сумма наибольших двух чисел введенных вами равна: {Sum_max_numb(Number_1, Number_2, Number_3)}')
input('Нажмите ENTER для завершения.')

