import sys, timeit


def usec(function, arguments):
    modname, funcname = __name__, function.__name__
    timer = timeit.Timer(stmt='%(funcname)s(*args)' % vars(),
                         setup='from %(modname)s import %(funcname)s; args=%(arguments)r' % vars())
    try:
        t, N = 0, 1
        while t < 0.2:
            t = min(timer.repeat(repeat=3, number=N))
            N *= 10
        microseconds = round(10000000 * t / N, 1) # per loop
        return microseconds
    except:
        timer.print_exc(file=sys.stderr)
        raise


def look_and_say(string):
    new_string = ""
    next_1 = ""
    next_2 = ""
    next_3 = ""
    for idx, letter in enumerate(string):
        #print(idx,new_string)
        if letter == '1':
            new_string = new_string + str(len(next_2)) + '2' if next_2 else new_string
            new_string = new_string + str(len(next_3)) + '3' if next_3 else new_string
            next_3 = ""
            next_2 = ""
            next_1 += "1"
        elif letter == '2':
            new_string = new_string + str(len(next_1)) + '1' if next_1 else new_string
            new_string = new_string + str(len(next_3)) + '3' if next_3 else new_string
            next_1 = ""
            next_3 = ""
            next_2 += "2"
        elif letter == '3':
            new_string = new_string + str(len(next_1)) + '1' if next_1 else new_string
            new_string = new_string + str(len(next_2)) + '2' if next_2 else new_string
            next_1 = ""
            next_2 = ""
            next_3 += "3"
    new_string = new_string + str(len(next_1)) + '1' if next_1 else new_string
    new_string = new_string + str(len(next_2)) + '2' if next_2 else new_string
    new_string = new_string + str(len(next_3)) + '3' if next_3 else new_string
    return new_string


conway_evolution = {
    'H' :	['H' ],
    'He': 	['Hf', 'Pa', 'H', 'Ca', 'Li'],
    'Li': 	['He'],
    'Be': 	['Ge', 'Ca', 'Li'],
    'B' :	['Be'],
    'C' :	['B' ],
    'N' :	['C' ],
    'O' :	['N' ],
    'F' :	['O' ],
    'Ne': 	['F' ],
    'Na': 	['Ne'],
    'Mg': 	['Pm', 'Na'],
    'Al': 	['Mg'],
    'Si': 	['Al'],
    'P' :	['Ho', 'Si'],
    'S' :	['P' ],
    'Cl': 	['S' ],
    'Ar': 	['Cl'],
    'K' :	['Ar'],
    'Ca': 	['K' ],
    'Sc': 	['Ho', 'Pa', 'H', 'Ca', 'Co'],
    'Ti': 	['Sc'],
    'V' :	['Ti'],
    'Cr': 	['V' ],
    'Mn': 	['Cr', 'Si'],
    'Fe': 	['Mn'],
    'Co': 	['Fe'],
    'Ni': 	['Zn', 'Co'],
    'Cu': 	['Ni'],
    'Zn': 	['Cu'],
    'Ga': 	['Eu', 'Ca', 'Ac', 'H', 'Ca', 'Zn'],
    'Ge': 	['Ho', 'Ga'],
    'As': 	['Ge', 'Na'],
    'Se': 	['As'],
    'Br': 	['Se'],
    'Kr': 	['Br'],
    'Rb': 	['Kr'],
    'Sr': 	['Rb'],
    'Y' :	['Sr', 'U'],
    'Zr': 	['Y' , 'H', 'Ca', 'Tc'],
    'Nb': 	['Er', 'Zr'],
    'Mo': 	['Nb'],
    'Tc': 	['Mo'],
    'Ru': 	['Eu', 'Ca', 'Tc'],
    'Rh': 	['Ho', 'Ru'],
    'Pd': 	['Rh'],
    'Ag': 	['Pd'],
    'Cd': 	['Ag'],
    'In': 	['Cd'],
    'Sn': 	['In'],
    'Sb': 	['Pm', 'Sn'],
    'Te': 	['Eu', 'Ca', 'Sb'],
    'I' :	['Ho', 'Te'],
    'Xe': 	['I' ],
    'Cs': 	['Xe'],
    'Ba': 	['Cs'],
    'La': 	['Ba'],
    'Ce': 	['La', 'H', 'Ca', 'Co'],
    'Pr': 	['Ce'],
    'Nd': 	['Pr'],
    'Pm': 	['Nd'],
    'Sm': 	['Pm', 'Ca', 'Zn'],
    'Eu': 	['Sm'],
    'Gd': 	['Eu', 'Ca', 'Co'],
    'Tb': 	['Ho', 'Gd'],
    'Dy': 	['Tb'],
    'Ho': 	['Dy'],
    'Er': 	['Ho', 'Pm'],
    'Tm': 	['Er', 'Ca', 'Co'],
    'Yb': 	['Tm'],
    'Lu': 	['Yb'],
    'Hf': 	['Lu'],
    'Ta': 	['Hf', 'Pa', 'H', 'Ca', 'W'],
    'W' :	['Ta'],
    'Re': 	['Ge', 'Ca', 'W'],
    'Os': 	['Re'],
    'Ir': 	['Os'],
    'Pt': 	['Ir'],
    'Au': 	['Pt'],
    'Hg': 	['Au'],
    'Tl': 	['Hg'],
    'Pb': 	['Tl'],
    'Bi': 	['Pm', 'Pb'],
    'Po': 	['Bi'],
    'At': 	['Po'],
    'Rn': 	['Ho', 'At'],
    'Fr': 	['Rn'],
    'Ra': 	['Fr'],
    'Ac': 	['Ra'],
    'Th': 	['Ac'],
    'Pa': 	['Th'],
    'U' :	['Pa']}


conway_string = {
    'H' :	22,
    'He': 	13112221133211322112211213322112,
    'Li': 	312211322212221121123222112,
    'Be': 	111312211312113221133211322112211213322112,
    'B':	1321132122211322212221121123222112,
    'C':	3113112211322112211213322112,
    'N':	111312212221121123222112,
    'O':	132112211213322112,
    'F':	31121123222112,
    'Ne': 	111213322112,
    'Na': 	123222112,
    'Mg': 	3113322112,
    'Al': 	1113222112,
    'Si': 	1322112,
    'P':	311311222112,
    'S':	1113122112,
    'Cl': 	132112,
    'Ar': 	3112,
    'K':	1112,
    'Ca': 	12,
    'Sc': 	3113112221133112,
    'Ti': 	11131221131112,
    'V':	13211312,
    'Cr': 	31132,
    'Mn': 	111311222112,
    'Fe': 	13122112,
    'Co': 	32112,
    'Ni': 	11133112,
    'Cu': 	131112,
    'Zn': 	312,
    'Ga': 	13221133122211332,
    'Ge': 	31131122211311122113222,
    'As': 	11131221131211322113322112,
    'Se': 	13211321222113222112,
    'Br': 	3113112211322112,
    'Kr': 	11131221222112,
    'Rb': 	1321122112,
    'Sr': 	3112112,
    'Y':    1112133,
    'Zr': 	12322211331222113112211,
    'Nb': 	1113122113322113111221131221,
    'Mo': 	13211322211312113211,
    'Tc': 	311322113212221,
    'Ru': 	132211331222113112211,
    'Rh': 	311311222113111221131221,
    'Pd': 	111312211312113211,
    'Ag': 	132113212221,
    'Cd': 	3113112211,
    'In': 	11131221,
    'Sn': 	13211,
    'Sb': 	3112221,
    'Te': 	1322113312211,
    'I':	311311222113111221,
    'Xe':   11131221131211,
    'Cs': 	13211321,
    'Ba': 	311311,
    'La': 	11131,
    'Ce': 	1321133112,
    'Pr': 	31131112,
    'Nd': 	111312,
    'Pm': 	132,
    'Sm': 	311332,
    'Eu': 	1113222,
    'Gd': 	13221133112,
    'Tb': 	3113112221131112,
    'Dy': 	111312211312,
    'Ho': 	1321132,
    'Er': 	311311222,
    'Tm': 	11131221133112,
    'Yb': 	1321131112,
    'Lu': 	311312,
    'Hf': 	11132,
    'Ta': 	13112221133211322112211213322113,
    'W':	312211322212221121123222113,
    'Re': 	111312211312113221133211322112211213322113,
    'Os': 	1321132122211322212221121123222113,
    'Ir': 	3113112211322112211213322113,
    'Pt': 	111312212221121123222113,
    'Au': 	132112211213322113,
    'Hg': 	31121123222113,
    'Tl': 	111213322113,
    'Pb': 	123222113,
    'Bi': 	3113322113,
    'Po': 	1113222113,
    'At': 	1322113,
    'Rn': 	311311222113,
    'Fr': 	1113122113,
    'Ra': 	132113,
    'Ac': 	3113,
    'Th': 	1113,
    'Pa': 	13,
    'U':	3}



def look_and_say_conway(molecule):
    new_molecule = list()
    for atom in molecule:
        new_molecule += conway_evolution[atom]
    return new_molecule


def look_and_say_conway_string(molecule):
    string_res = ''
    for elem in molecule:
        string_res += str(conway_string[elem])
    return string_res


def classic_way(input,iter):
    for loop in range(iter):
        input = look_and_say(input)
    return input


def conway_way(input,iter):
    for loop in range(iter):
        input = look_and_say_conway(input)
    return input


if __name__ == '__main__':

    input = "1113222113" # = Po !
    c_input = ['Po']

    print("Conway Style")
    print("10  ",usec(conway_way, (c_input, 10)))
    print("20  ",usec(conway_way, (c_input, 20)))
    print("30  ",usec(conway_way, (c_input, 30)))
    print("40  ",usec(conway_way, (c_input, 40)))
    print("50  ",usec(conway_way, (c_input, 50)))

    print("Classic Style")
    print("10  ",usec(classic_way, (input, 10)))
    print("20  ",usec(classic_way, (input, 20)))
    print("30  ",usec(classic_way, (input, 30)))
    print("40  ",usec(classic_way, (input, 40)))

    print("Results length:")
    print("40 :", len(look_and_say_conway_string(conway_way(c_input, 40))))
    print("50 :", len(look_and_say_conway_string(conway_way(c_input, 50))))



