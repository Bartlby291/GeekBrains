import random
import os
file = open('Path_2_counting_words.txt', 'a')
def generate_str_list():
    source_list = ['поле', 'лес', 'поляна', 'горы']
    generate_list =[]
    while len(generate_list) < random.randint(5, 10):
        generate_list.append(random.choice(source_list))
    return generate_list
count = 0
while count < random.randint(6, 10):
    for el in generate_str_list():
        file.write(f'{el} ')
    file.write('\n')
    count += 1
file.close()
file = open('Path_2_counting_words.txt')
for numb, line in enumerate(file.readlines(), 1):
    print(f'В строке: {numb}. {len(line.split())} слов')
file.close()
os.remove('Path_2_counting_words.txt')






file.close()
