from utils import read
import re
import math

def parse(input):
    times = [int(value) for value in re.findall(r"\d+", input[0])]
    dist = [int(value) for value in re.findall(r"\d+", input[1])]

    return {
        "time" : times,
        "dist" : dist
    }
def get_product(l):
    out = 1
    for e in l:
        out *= e
    return out

def get_n_ways(input):
    numb_ways = []

    for j in range(len(input["time"])):
        c = 0
        pairs = (input["time"][j], input["dist"][j])
        for i in range(1, pairs[0] - 1):
            cur_range = i * (pairs[0] - i)
            if cur_range > pairs[1]:
                c += 1
        numb_ways.append(c)
    return numb_ways

r = parse(read("6/6.txt").splitlines())
print(get_product(get_n_ways(r)))
print(get_product(get_n_ways(parse(read("6/6.txt").replace(" ", "").splitlines()))))