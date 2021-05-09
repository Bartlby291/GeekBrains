def Calculate(x, y, act):
    if act == '+':
        z = x + y
        return print(f'Сумма чисел равна {z}')
    elif act == '-':
        z = x - y
        return print(f'Разность чисел равна {z}')
    elif act == '*':
        z = x * y
        return print(f'Умножение чисел равно {z}')
    elif act == '/':
        if y == 0:
            return print('Деление на ноль запрещено.')
        else:
            z = x / y
            return print(f'Деление чисел равно {round(z, 3)}')
    else:
        return print('Вы указали неверную команду')

def user_input():
    Number_1 = None
    while Number_1 == None:
        try:
            Number_1 = float(input('Введите число >>> '))
        except ValueError:
            print('Вы вели не число, попробуйте еще раз')
    Action = input('Введите необходимое действие в формате: +, -, *, / >>> ')
    Number_2 = None
    while Number_2 == None:
        try:
            Number_2 = float(input('Введите число >>> '))
        except ValueError:
            print('Вы вели не число, попробуйте еще раз')
    Calculate(Number_1, Number_2, Action)
while True:
    user_input()
    exit_key = input('Нажмите ENTER для продолжения использовани или "@"+ENTER для выхода')
    if exit_key == '@':
        print('Досвидания')
        break

