def Cheng_register(text):
    text = text.split(' ')
    modified_text = ''
    for el in text:
        el = el[0].upper() + el[1:]
        modified_text += f'{el} '
    return modified_text
User_input = input('Введите слово в котором все буквы находятся в нижнем регистре >>> ')
print(Cheng_register(User_input))
input('Нажмите ENTER для завершения.')
