def exponentiation(a, x):
    return a ** x


def exponentiation_in_cycle(a, x):
    b = abs(x)
    z = a
    if x == b:
        for i in range(1, b):
            a = a * z
        return a
    else:
        for i in range(1, b):
            a = a * z
        return 1 / a


Number_1 = None
while Number_1 == None:
    try:
        Number_1 = float(input('Введите действительное положительное число >>> '))
    except ValueError:
        print('Вы вели не число, попробуйте еще раз')
Number_2 = None
while Number_2 == None:
    try:
        Number_2 = int(input('Введите целое отрицательное число >>> '))
    except ValueError:
        print('Введенное число не отвечает требованиям')
print(f'Результат возведения в степень при помощи оператора **: {exponentiation(Number_1, Number_2)}')
print(f'Результат возведения в степень при помощи цикла: {exponentiation_in_cycle(Number_1, Number_2)}')
input('Нажмите ENTER для завершения.')
