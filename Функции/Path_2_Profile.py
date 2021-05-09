def User_profile(Name, Surname, Year, Town, Email, Phone):
    return print(f'Приветствую, {Surname} {Name}, родившись в {Year} году, в городе {Town}, вами было получено право '
                 f'получать электронные письма на адрес: {Email} и принимать звонки на номер: {Phone}')


User_name = input('Введите ваше имя >>> ')
User_surname = input('Введите вашу фамилию >>> ')
User_year = input('Введите год вашего рождения >>> ')
User_town = input('Введите названия города где вы роделись >>> ')
User_email = input('Ваш Email >>> ')
User_phone = input('Номер вашего телефона >>> ')
User_profile(Name=User_name, Surname=User_surname, Year=User_year, Town=User_town, Email=User_email, Phone=User_phone)
input('Нажмите ENTER для завершения.')
