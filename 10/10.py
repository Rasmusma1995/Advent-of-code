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


d2 = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def find_start(input):

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "S":
                return (i,j)

def find_longest_path(input):
    start = find_start(input)
    q = deque([[start, 0]])
    visisted = {(start)}
    arr = [["." for n in range(len(input[0]))] for n in range(len(input))]

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
            arr[next_field[0]][next_field[1]] = d
            visisted.add(next_field)

    return d, arr


print(find_longest_path(r)[0])
arr = find_longest_path(r)[1]

def is_point_enclosed(arr, point, visited, p=set()):
    row = len(arr)
    c = len(arr[0])
    x, y = point
    if x < 0 or x >= row or y < 0 or y >= c:
        return False, p

    if (x,y) in visited:
        return True, p

    visited.add((x, y))

    if arr[x][y] != ".":
        print(123)
        #p.add((x, y))
        print(123)
        return True, p

    tmp = True

    for i, j in d2:
        next_i, next_j = x + i, y + j
        t = is_point_enclosed(arr, (next_i, next_j), p)
        print(t)
        tmp &= t[0]

    return tmp, p

def check_p(arr, point):
    row = len(arr)
    c = len(arr[0])
    visited = set()
    perimeter = set()

    return is_point_enclosed(arr, point, visited, perimeter)


c  = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == ".":
            t = check_p(arr, (i,j))
            print(t)
           # c += check_p(arr, (i,j))

print(c)
k =check_p(arr, (6,14))

