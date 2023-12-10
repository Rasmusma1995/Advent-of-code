from utils import read
import re
from utils import operator_f

def parser(input):
    out = []
    for l in input:
        out.append([int(e) for e in re.findall(r"-?\d+", l)])
    return out


def expand(input):
    first_iter = [input]
    for j in range(len(input)):
        tmp = [first_iter[j][i + 1] - first_iter[j][i] for i in range(0, len(first_iter[j]) - 1, 1)]
        first_iter.append(tmp)
        if all(e == 0 for e in tmp):
            break
    return first_iter

def get_sum_of_line(iter_list,symbol="+"):
    last_val = 0
    sum = 0
    for line in iter_list[::-1]:
        curr_val = line.pop()
        sum = operator_f(symbol, curr_val, last_val)
        last_val = sum
    return sum

def rev_expanded_list(el):
    out = []
    for l in el:
        out.append(l[::-1])
    return out


def p1(input):
    return sum([get_sum_of_line(expand(l)) for l in r])

def p2(input):
    return sum([get_sum_of_line(rev_expanded_list(expand(l)),"-") for l in r])


r = parser(read("9/9.txt").splitlines())
print(p1(r))
print(p2(r))