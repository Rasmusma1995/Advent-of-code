from utils import read
import re
import math
r = read("4\\4.txt").splitlines()

def get_number_of_w(line):
    num = line.split(":")[1].split("|")
    have = [int(e) for e in re.findall(r"\d+", num[1])]
    winning  = [int(e) for e in re.findall(r"\d+", num[0])]
    c = 0
    for h in have:
        if h in winning :
            c+= 1
    return c

def get_n_points(line):
    c = get_number_of_w(line)
    if c == 0:
        return 0
    out = 1
    for i in range(1, c) :
        out *= 2
    return out

def get_total_of_scracted_cards(input):
    cards = [1 for l in range(len(input))]
    for index, l in enumerate(input):
        c = get_number_of_w(l)
        for j in range(1, c + 1):
            cards[index + j] += cards[index]
    return sum(cards)


print(sum([get_n_points(l) for l in r]))
print(get_total_of_scracted_cards(r))

