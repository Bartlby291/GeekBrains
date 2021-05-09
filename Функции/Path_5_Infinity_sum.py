Full_list = []
def Infinity_sum():
    User_input = (input(f'Ведите любое количество чисел через пробел. '
                       f'Для завершения в любой момент ввода напишите "@">> ').split(' '))
    Full_list.extend(User_input)
    Sum = 0
    for i in Full_list:
        if i == '@':
            return print(f'Программа завершена. Результат суммирования равен: {Sum} ')

        else:
            try:
                i = int(i)
            except:
                print(f'Символ "{i}" не является числом')
                print(f'Промежеточная сумма чисел равна: {Sum}')
                Full_list.remove(i)
                Infinity_sum()
            Sum += i
    print(f'Промежеточная сумма чисел равна: {Sum}')
    Infinity_sum()
Infinity_sum()
input('Нажмите ENTER для завершения.')