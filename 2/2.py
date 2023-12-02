from utils import read

vec_g = [str_v.split(":",1)[-1].strip() for str_v in read("2\\2.txt").split("\n")]

restric_for_possible_games = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

def get_number_of_occ(string):
    l = [e.strip().split(" ") for e in string.split(";")]

    out = []
    for e in l:
        color_count = {}
        for index in range(0, len(e), 2):
            color = e[index + 1].replace(",", "")
            count = int(e[index])
            if color in color_count:
                color_count[color] += count
            else:
                color_count[color] = count
        out.append(color_count)
    return out

def is_game_possible(g):
    occ = get_number_of_occ(g)
    for color, count in restric_for_possible_games.items():
        for o in occ:
            if o.get(color):
                if o.get(color)>count:
                    return False
    return True

def get_power_set_of_game(g_element):
    g = get_number_of_occ(g_element)
    min_set = {}
    for e in g:
        for color, count in e.items():
            if color not in min_set:
                min_set[color] = count
            elif min_set.get(color) < count:
                min_set[color] = count

    power_set = 1
    for v in min_set.values():
        power_set *= v
    return power_set

print(sum([get_power_set_of_game(g) for g in vec_g]))
print(sum([index+1 for index, g in enumerate(vec_g) if is_game_possible(g)]))