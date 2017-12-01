

if __name__ == '__main__':
    tot_code_len = 0
    tot_mem_len = 0

    debug = False
    if not debug:
        lines = list()
        with open('input', 'r') as f:
            for line in f:
                lines.append(line[:-1])
    else:
        lines = list()
        lines.append("\"\"")
        lines.append("\"abc\"")
        lines.append("\"aaa\\\"aaa\"")
        lines.append("\"\\x27\"")

    for line in lines:
        code_len = len(line)
        exec("mem_len = len("+line+")")
        tot_mem_len += mem_len
        tot_code_len += code_len

    print("part1 result =", tot_code_len - tot_mem_len)

    tot_new_encoded = 0
    for line in lines:
        new_encoded = len(line) + 2
        for c in line:
            if c in ['\\', '\"']:
                new_encoded += 1
        tot_new_encoded += new_encoded

    print("part2 result =", tot_new_encoded - tot_code_len)
