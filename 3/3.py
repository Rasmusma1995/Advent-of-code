from utils import read
import numpy as np
import math
import re

input = read("3/3.txt").splitlines()
directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
]

def get_value_in_dir(x, y, dir,input_d):
    nx = x + dir[0]
    ny = y + dir[1]
    if not 0 <= nx < len(input_d):
        return None

    if not 0 <= ny < len(input_d[0]):
        return None

    return input_d[nx][ny]


def where_is_number_with_adjent_symbols(d):
    arr = np.zeros(shape=(len(d), len(d[0])))

    for i, r in enumerate(d):
        for j, c in enumerate(r):
            if c.isdigit():
                for di in directions:
                    val = get_value_in_dir(i, j , di, d)
                    if val is None:
                        continue
                    if val == "." or val.isdigit():
                        continue
                    arr[i][j] = 1

    return arr

def get_relevant_numbers(input):
    arr = where_is_number_with_adjent_symbols(input)
    numbers = []
    for index, line in enumerate(input):
        for y in re.finditer(r"\d+",line):
            x = y.start()
            y = y.end()
            m = max(arr[index][x:y])
            if m > 0 :
                numbers.append(int(input[index][x:y]))
    return numbers

#part 2

def number_pos(input):
    numbers = []
    for index, line in enumerate(input):
        for y in re.finditer(r"\d+",line):
            x = y.start()
            y = y.end()
            numbers.append([index, x,y, int(line[x:y])])
    return numbers

def get_number(x,y, input, l):
    for e in l:
        if x == e[0] and e[1] <= y < e[2]:
            return e[3], (e[0], e[1],e[2])

def get_sum_of_gear_product(d,l):
    sum = 0
    for i, r in enumerate(d):
        for j, c in enumerate(r):
            if c == "*":
                s = set()
                for di in directions:
                    val = (get_number(i + di[0], j + di[1], d, l))
                    if val is None:
                        continue
                    s.add(val)
                if len(s) >1 :
                    sum += math.prod([v[0] for v in s])

    return sum

print(sum(get_relevant_numbers(input)))
print(get_sum_of_gear_product(input, number_pos(input)))



