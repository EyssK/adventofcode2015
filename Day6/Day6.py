
def apply_cmd(cmd, start, stop ):
    start = [int(coord) for coord in start.split(',')]
    stop = [int(coord) for coord in stop.split(',')]
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            grid[x][y] = actions[cmd](grid[x][y])

if __name__ == '__main__':
    grid = [[0] * 1000 for _ in range(1000)]
    actions = {
        'toggle': lambda x: x+2,
        'turn on': lambda x: x+1,
        'turn off': lambda x: x-1 if x > 0 else 0
    }
    with open("input","r") as f:
        for line in f:
            cmd, start, _,stop = line.strip().rsplit(' ',3)
            apply_cmd(cmd, start, stop )

    flattened = [val for sublist in grid for val in sublist]
    print(sum(flattened))

