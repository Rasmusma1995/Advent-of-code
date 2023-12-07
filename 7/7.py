from utils import read
import copy

rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
rank_dict = {rank[i]: i for i in range(len(rank))}

rank2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
rank_dict2 = {rank2[i]: i for i in range(len(rank2))}

def sort_function(string,dict_input):
    v = 1
    for char in string:

        t = dict_input.get(char)
        if t==0:
            v *= 10000
        else:
            v = v*10000 + t
    return v

def get_inner_rank(tmp_input):
    inner_rank = 1

    if 5 in tmp_input.values():
        inner_rank = 7
    elif 4 in tmp_input.values():
        inner_rank = 6
    elif 2 in tmp_input.values() and 3 in tmp_input.values():
        inner_rank = 5
    elif 3 in tmp_input.values():
        inner_rank = 4
    elif 2 in tmp_input.values() and list(tmp_input.values()).count(2) == 2:
        inner_rank = 3
    elif 2 in tmp_input.values():
        inner_rank = 2

    return inner_rank

def create_dict_from_hand(hand):
    tmp = {}
    for letter in hand:
        if letter in tmp:
            tmp[letter] += 1
        else:
            tmp[letter] = 1
    return tmp

def get_score_for_out(out):

    sort_v= sorted(out, key=lambda x: x[2])
    sum = 0
    for index, k in enumerate(sort_v):
        sum += (index+1)*k[0]
    return sum

def p1(input):

    bid = [int(l.split(" ")[1]) for l in input]
    hand = [l.split(" ")[0] for l in input]

    paired_list = sorted(zip(bid, hand), key=lambda x: sort_function(x[1], rank_dict), reverse=True)

    out=[]
    for l in paired_list:
        tmp = create_dict_from_hand(l[1])
        out.append((l[0],l[1],get_inner_rank(tmp)))


    return get_score_for_out(out)

# Part 2

def p2(input):

    bid = [int(l.split(" ")[1]) for l in input]
    hand = [l.split(" ")[0] for l in input]

    paired_list = sorted(zip(bid, hand), key=lambda x: sort_function(x[1], rank_dict2), reverse=True)

    out=[]
    for l in paired_list:
        tmp = create_dict_from_hand(l[1])
        n_jokers = tmp.get("J")
        if n_jokers:
            max_inner_rank = get_inner_rank(tmp)
            for t in tmp.keys():
                ny_tmp = copy.deepcopy(tmp)
                v = ny_tmp.pop("J")
                if t in ny_tmp:
                    ny_tmp[t] += v
                else:
                    ny_tmp[t] = v
                ny_tmp_rank = get_inner_rank(ny_tmp)
                max_inner_rank = max(max_inner_rank,ny_tmp_rank)
            out.append((l[0], l[1], max_inner_rank))

        else:
            out.append((l[0],l[1],get_inner_rank(tmp)))


    return get_score_for_out(out)

r = read("7/7.txt").splitlines()
print(p1(r))
print(p2(r))
