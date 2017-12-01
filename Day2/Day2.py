import re


def paper_surface(a,b,c):
    surfaces = [a*b,a*c,b*c]
    return 2*sum(surfaces)+min(surfaces)


def ribbon_length(a,b,c):
    sorted = [a,b,c]
    sorted.sort()
    return 2*sum(sorted[0:2])+a*b*c


def find_lengths(string):
    res = re.match("([0-9]+)x([0-9]+)x([0-9]+)", string)
    return [int(res.group(1)), int(res.group(2)), int(res.group(3))]


if __name__ == '__main__':
    total_surface = 0
    total_ribbon = 0
    with open("input","r") as f:
        for idx,line in enumerate(f):
            lengths = find_lengths(line)
            total_surface += paper_surface(lengths[0],lengths[1],lengths[2])
            len = ribbon_length(lengths[0],lengths[1],lengths[2])
            #print(lengths,len)
            total_ribbon += len
            #if idx == 1:
            #    break

    print( "total_surface", total_surface )
    print("total_ribbon", total_ribbon)