import random
source_list = []
while len(source_list) < 10:
    source_list.append(random.randint(1, 300))
print(f'Исходный список: {source_list}')
previous_el = 0
result_list = []
for el in source_list:
    if previous_el > el:
        result_list.append(previous_el)
    previous_el = el
print(f'Результат: {result_list}')
