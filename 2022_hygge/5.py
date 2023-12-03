from collections import deque
from utils import read
import re
from functools import lru_cache



r = read("2022_hygge/5.txt").splitlines()

def get_number_of_stack(input):
    max_n = 0
    for line in input:
        if "[" not in line:
            break
        n = sum(1 for char in line if char.isalpha())
        max_n = max(n,max_n)
    return max_n

def fill_stacks(input):
    n_stacks = get_number_of_stack(r)
    stack_list = [deque() for i in range(n_stacks)]
    for line in input:
        if "[" not in line:
            break
        s = 0
        for index in range(0, n_stacks * 3+100, 4):
            crate = line[index:index + 3]
            if "[" in crate:
                stack_list[s].append(crate)
            s += 1
    return stack_list

def get_moves(input):
    out = []
    for line in input:
        if "[" in line:
            continue
        if "move" in line:
            tmp = [int(e) for e in re.findall(r'\d+', line)]
            out.append(tmp)
    return out

def move_stacks(input):
    m = get_moves(input)
    filled_stacks = fill_stacks(input)
    for e in m:
        n_moves = e[0]
        from_stack = e[1] - 1
        to_stack = e[2] - 1
        for j in range(n_moves):
            filled_stacks[to_stack].appendleft(filled_stacks[from_stack].popleft())
    return filled_stacks

def move_stacks_order(input):
    m = get_moves(input)
    filled_stacks = fill_stacks(input)
    for e in m:
        n_moves = e[0]
        from_stack = e[1] - 1
        to_stack = e[2] - 1
        crate_list = [filled_stacks[from_stack].popleft() for j in range(n_moves)]
        for v in crate_list[::-1]:
            filled_stacks[to_stack].appendleft(v)
    return filled_stacks


def print_top(input,move_stack_f):
    n_stacks = get_number_of_stack(input)
    mov = move_stack_f(input)
    str = ""
    for i in range(n_stacks):
        v = mov[i].popleft()
        str += v

    return str.replace("[","").replace("]","")

print(print_top(r, move_stacks))
print(print_top(r, move_stacks_order))