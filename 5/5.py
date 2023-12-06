from utils import read
import re
import string

def contains_a_letters(s):
    set_v = set(string.ascii_lowercase)
    return any(v in set_v for v in s)

def parser(input):
    d = {}
    d['seeds'] = [int(value) for value in re.findall(r"\d+", input[0])]

    j = 2
    while j<len(input):
        if contains_a_letters(input[j]):
            key = input[j]
        else:
            vals = [int(v) for v in re.findall(r"\d+", input[j])]
            if vals == []:
                j += 1
                continue
            if key in d:
                d[key].append(vals)
            else:
                d[key] = [vals]
            #
        j += 1

    return d

def get_min_out(r,seed_values):
    out = []
    for s in seed_values:
        for v in r.keys():
            if v == "seeds":
                continue
            maps = r.get(v)
            for m in maps:
                dest = m[0]
                source = m[1]
                range = m[2]
                if source <= s < source + range:
                    place = s - source
                    s = dest + place
                    break
        out.append(s)
    return min(out)


def parser(input):
    d = {}
    d['seeds'] = [int(value) for value in re.findall(r"\d+", input[0])]

    j = 2
    while j<len(input):
        if contains_a_letters(input[j]):
            key = input[j]
        else:
            vals = [int(v) for v in re.findall(r"\d+", input[j])]
            if vals == []:
                j += 1
                continue
            if key in d:
                d[key].append(vals)
            else:
                d[key] = [vals]
            #
        j += 1

    return d


r = parser(read("5/5.txt").splitlines())

#part 2
def make_new_seed_values(r): #used for brute
    s = r.get("seeds")
    new_seeds = [s[i] + v for i in range(0, len(s), 2) for v in range(s[i + 1])]

    return new_seeds

def create_map_dict(a=[],b=[]):
    return {
        "mapped" : a,
        "nmapped" : b
    }

def get_mapped_nmapped(int_v, split_int):

    if split_int[0] <= int_v[0] <= int_v[1] <= split_int[1] :
        return create_map_dict(int_v)
    if int_v[0] > split_int[1] or int_v[1] < split_int[0]:
        return create_map_dict(b=int_v)

    a = (max(int_v[0], split_int[0]), min(int_v[1], split_int[1]))
    b = []
    if int_v[0] < split_int[0]:
        b.extend((int_v[0], split_int[0] - 1))
    if int_v[1] > split_int[1]:
        b.extend((split_int[1] + 1, int_v[1]))

    return create_map_dict(a, b)

def get_lowest_location_p2(input):
    s = input.get("seeds")

    pair = [(s[i], s[i] + s[i + 1] - 1) for i in range(0, len(s), 2)]

    out = []
    for p in pair:
        notmapped = [p]
        for v in input.keys():
            if v == "seeds" or not contains_a_letters(v):
                continue
            maps = input.get(v)
            mapped = []
            for m in maps:
                si = (m[1], m[1] + m[2] - 1)
                tmp = []
                while notmapped:
                    interval = notmapped.pop()
                    si_split = get_mapped_nmapped(interval, si)
                    mi = si_split["mapped"]
                    nmi = si_split["nmapped"]
                    if mi:
                        k = mi[0] - si[0]
                        mapped.append((m[0] + k, m[0] + k + (mi[1] - mi[0])))
                    for j in range(0, len(nmi), 2):
                        tmp.append((nmi[j], nmi[j + 1]))

                notmapped = tmp
            notmapped += mapped
        out.extend(notmapped)

    return (min(v[0] for v in out))

print(get_min_out(r, r.get("seeds")))
print(get_lowest_location_p2(r))

