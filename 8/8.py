from utils import read
import re
import math
from functools import reduce


def move_dir(s):
    if s == "L":
        return 0
    return 1

def parser(input):
    dirc = input[0]
    d = {}
    for i in range(2, len(input)):
        tmp = re.findall(r'\b\w{3}\b', input[i])
        d[tmp[0]] = tmp[1:3]

    return dirc, d


r = parser(read("8/8.txt").splitlines())

def p1(input,startnode, end="ZZZ"):
    j = 0
    c = 0
    node = startnode
    tree = input[1]
    dirc = input[0]
    while True:
        if j >= len(dirc):
            j = 0
        cur_dirc = dirc[j]
        node = tree.get(node)[move_dir(cur_dirc)]
        c += 1
        j += 1
        tmp = node[::-1]
        if tmp[0:len(end)] == end:
            break

    return c


#part 2

def lcm(arr):
    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l


def p2(input):
    v = [p1(input,e, "Z") for e in input[1].keys() if e[2] == "A"]

    return lcm(v)

print(p1(r, "AAA"))
print(p2(r))
