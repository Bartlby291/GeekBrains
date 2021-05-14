from functools import reduce
source_range = [el for el in range(99, 1001) if el % 2 == 0]
def multiply(prev_el, el):
    return prev_el * el
print(reduce(multiply, source_range))