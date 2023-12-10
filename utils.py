import os
import operator

def read(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, name)
    with open(file_path, 'r') as f:
        content = f.read()
    return content




def operator_f(symbol, a,b):
    operator_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    f = operator_map.get(symbol)
    return f(a,b)