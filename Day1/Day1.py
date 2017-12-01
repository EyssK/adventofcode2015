import re


def count_floors(string):
    return len(re.findall("\(",string)) - len(re.findall("\)",string))


def seq_floor(string):
    pos = 0
    for idx,c in enumerate(string):
        pos = pos+1 if c == '(' else pos-1
        if pos == -1:
            return idx+1


if __name__ == '__main__':
    full_file = ''
    with open("input","r") as f:
        for line in f:
            full_file += line
    print( count_floors(full_file))
    print(seq_floor(full_file))