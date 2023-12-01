from utils import read

vec = read("1\\1.txt").split("\n")
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_number(str):
    try:
        for char in str:
            if char.isdigit():
                return int(char)
    except:
        return 0

def replace_words(str_input):
    for index, w in enumerate(words):
        str_input = str_input.replace(w, w[0] + str(index+1) + w[-1])
    return str_input

def cal_sum(vec_input):
    result = 0
    for v in vec_input:
        result += get_number(v) * 10 + get_number(v[::-1])
    return result

print(cal_sum(vec))
print(cal_sum([replace_words(v) for v in vec]))