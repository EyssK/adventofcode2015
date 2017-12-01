
cmds = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y,
    "NOT": lambda x: 65535 - x
}

lines = list()
lines.append("123 -> x       ")
lines.append("456 -> y       ")
lines.append("x AND y -> d   ")
lines.append("x OR y -> e    ")
lines.append("x LSHIFT 2 -> f")
lines.append("y RSHIFT 2 -> g")
lines.append("NOT x -> h     ")
lines.append("NOT y -> i     ")


def link_circuit(cmd_line, out, circuit):
    cmd_list = cmd_line.split()
    args = []
    cmd = 0
    for i in cmd_list:
        if i in cmds:
            cmd = cmds[i]
        elif i in circuit and circuit[i].isdigit():
            args.append(int(circuit[i]))
        elif i.isdigit():
            args.append(int(i))
        else :
            # unresolved yet
            circuit[out] = cmd_line
            return
    if cmd:
        circuit[out] = str(cmd(*args))
    else:
        circuit[out] = str(args[0])


if __name__ == '__main__':
    circuit = dict()
    with open('input','r') as f:
        for line in f:
            cmd, _, out = line.strip().rsplit(' ',2)
            link_circuit(cmd,out,circuit)
    while circuit['a'].isdigit() == False:
        for out, cmd in circuit.items():
            link_circuit(cmd, out, circuit)
    answer_a = circuit['a']
    print('a signal is :',answer_a )

    circuit = dict()
    with open('input', 'r') as f:
        for line in f:
            cmd, _, out = line.strip().rsplit(' ', 2)
            link_circuit(cmd, out, circuit)
    circuit['b'] = answer_a
    while circuit['a'].isdigit() == False:
        for out, cmd in circuit.items():
            link_circuit(cmd, out, circuit)
    print('new a signal is :', circuit['a'])

