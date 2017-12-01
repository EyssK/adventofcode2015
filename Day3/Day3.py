

def list_visited(position, visited_houses, string):
    for c in string:
        if c == '^':
            position = (position[0], position[1]+1)
        elif c == '>':
            position = (position[0]+1, position[1])
        elif c == '<':
            position = (position[0]-1, position[1])
        elif c == 'v':
            position = (position[0], position[1]-1)
        else:
            print("ERROR: unknown char",c)
        visited_houses.append(position)
    return position

def nb_house_passed(file):
    visited_houses = [(0, 0)]
    with open(file, "r") as f:
        for line in f:
            list_visited((0,0),visited_houses,line)
    # remove doubles
    visited_houses = set(visited_houses)
    return len(visited_houses)


def santa_and_robot(file):
    visited_houses = [(0, 0)]
    with open(file, "r") as f:
        for line in f:
            list_visited((0, 0), visited_houses, line[1::2])
            list_visited((0, 0), visited_houses, line[0::2])
    # remove doubles
    visited_houses = set(visited_houses)
    return len(visited_houses)


if __name__ == '__main__':
    s = nb_house_passed("input")
    print("santa=", s)
    sar = santa_and_robot("input")
    print("robot+santa=",sar)