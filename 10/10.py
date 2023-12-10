from collections import deque
from utils import read

r = read("10/10.txt").splitlines()

#row first column second
directions =  {
    '|': [(1,0),(-1,0)],
    '-': [(0,1),(0,-1)],
    'L': [(-1,0), (0,1)],
    'J': [(0,-1), (-1,0)],
    '7': [(1,0), (0,-1)],
    'F': [(0,1), (1,0)],
    'S': [(1,0), (0,1)]
}

def find_start(input):

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "S":
                return (i,j)

def p1(input):
    start = find_start(input)
    q = deque([[start, 0]])
    visisted = {(start)}

    while q:
        field, d = q.popleft()
        for dir in directions.get(input[field[0]][field[1]]):
            next_field = (field[0] + dir[0], field[1] + dir[1])
            if next_field[0] >= len(input) or next_field[1] >= len(input[0]):
                continue

            v = input[next_field[0]][next_field[1]]
            if next_field in visisted or v == ".":
                continue
            q.append([next_field, d + 1])
            visisted.add(next_field)

    return d


print(p1(r))