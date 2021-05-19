import os
def write_file():
    user_inp = input('Введите данные >>> ')
    if user_inp == '':
        try:
            with open('User_input.txt') as file:
                print(f'Содержание файла: {file.read()}')
        except:
            print('Файла не существует')
        print('Файл удален с вашего ПК')
        os.remove('User_input.txt')
        exit()
    with open('User_input.txt', 'a+') as file:
        file.write(f'{user_inp}\n')
    with open('User_input.txt') as file:
        print(f'Содержание файла: \n{file.read()}')
    write_file()
write_file()
