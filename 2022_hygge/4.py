from utils import read

d = read("2022_hygge/4.txt").splitlines()

def make_interval(input_list):
    out = []
    index = 0
    for e in input_list:
        for e1 in e.split(","):
            range_parts =  map(int, e1.split("-"))
            tmp = (index, tuple(range_parts))
            out.append(tmp)
        index += 1
    return out


def n_check_complete_contained(interval_list):

    n = 0
    for index in range(0,len(interval_list),2):
        alf1 = interval_list[index][1]
        alf2 = interval_list[index+1][1]
        if alf1[0] <= alf2[0] <= alf2[1] <= alf1[1] or alf2[0] <= alf1[0] <= alf1[1] <= alf2[1] :
            n += 1
    return n


def n_check_overllaped(interval_list):

    n = 0
    for index in range(0,len(interval_list),2):
        alf1 = interval_list[index][1]
        alf2 = interval_list[index+1][1]
        if alf1[0] <= alf2[0]  <= alf1[1] \
                or  alf1[0] <= alf2[1]  <= alf1[1] \
                or alf2[0] <= alf1[0] <= alf2[1]  \
                or  alf2[0] <= alf1[1] <= alf2[1]:
            n += 1
    return n



l = make_interval(d)
print(n_check_complete_contained(l))
print(n_check_overllaped(l))
