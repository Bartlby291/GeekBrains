import os
translate_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}
with open('Path_4_dict.txt') as file:
    file_dict = file.readlines()
for line in file_dict:
    line_list = line.split(' - ')
    with open('Path_4_translate.txt', 'a') as file:
        file.write(f'{translate_dict[line_list[0]]} - {line_list[1]}')
with open('Path_4_translate.txt') as file:
    print(file.read())
os.remove('Path_4_translate.txt')
