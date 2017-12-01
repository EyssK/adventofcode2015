import itertools

debug = False
lines = list()
if debug:
    lines.append("London to Dublin = 464")
    lines.append("London to Belfast = 518")
    lines.append("Dublin to Belfast = 141")
else:
    with open("input", "r") as f:
        for line in f:
            lines.append(line)


if __name__ == '__main__':
    dist_tree = dict()

    for line in lines:
        c_from, _, c_to, _, dist = line.strip().split(' ')
        dist = int(dist)
        if c_from in dist_tree :
            dist_tree[c_from][c_to] = dist
        else:
            dist_tree[c_from] = {c_to:dist}

        if c_to in dist_tree:
            dist_tree[c_to][c_from] = dist
        else:
            dist_tree[c_to] = {c_from:dist}

    min_path_dist = 1000000
    max_path_dist = 0
    for path in itertools.permutations(dist_tree):
        path_dist = 0
        for idx, city in enumerate(path[:-1]):
            path_dist += dist_tree[city][path[idx+1]]
        if path_dist < min_path_dist:
            min_path_dist = path_dist
            min_path = path
        if path_dist > max_path_dist:
            max_path_dist = path_dist
            max_path = path
    print("--- MIN PATH ---")
    print(min_path)
    print(min_path_dist)
    print("--- MAX PATH ---")
    print(max_path)
    print(max_path_dist)


