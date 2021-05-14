import sys
try:
    file, arg_user, arg_bet, arg_prize, arg_hours = sys.argv
except:
    print('Неверные параметры')
    exit()

def calc_salary(user, bet, prize, hours):
    try:
        int(bet)
    except:
        print(f'Параметр "{bet}" не является значением "Ставка в час"')
        exit()
    try:
        float(prize)
    except:
        print(f'Параметр "{prize}" не является значением "Премия"')
        exit()
    try:
        int(hours)
    except:
        print(f'Параметр "{hours}" не является значением "Выработка в часах"')
        exit()
    salary = int(bet) * int(hours) * float(prize)
    print(f'{user}, ваша заработная плата с учетом премии составляет: {round(salary, 2)}.')
calc_salary(arg_user, arg_bet, arg_prize, arg_hours)