import random
import os
random_list = []
random_str = ''
while len(random_list) < 15:
    random_list.append(random.randint(1, 50))
for el in random_list:
    random_str = f'{random_str} {el}'
with open('Path_5_generate_sum.txt', 'w') as file:
    file.write(random_str)
with open('Path_5_generate_sum.txt') as file:
    file_str = file.read()
file_str = file_str.split()
file_sum = 0
for numb in file_str:
    file_sum += int(numb)
print(file_sum)
os.remove('Path_5_generate_sum.txt')

