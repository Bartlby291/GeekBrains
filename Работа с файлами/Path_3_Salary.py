import random
import os
file = open('Path_3_salary.txt')
result_file = open('Path_3_salary_result.txt', 'a')
for line in file.readlines():
    rline = line.split('\n')
    result_file.write(f'{rline[0]} {random.randint(10000, 30000)}\n')
file.close()
result_file.close()
result_file = open('Path_3_salary_result.txt')
salary_sum = 0
for line in result_file.readlines():
    if int(line.split()[1]) < 20000:
        print(line, end='')
    salary_sum += int(line.split()[1])
with open('Path_3_salary_result.txt') as file:
    str_count = (len(file.readlines()))
average_salary = salary_sum / str_count
print(f'Средняя ЗП составляет: {round(average_salary, 2)}')
result_file.close()
os.remove('Path_3_salary_result.txt')
