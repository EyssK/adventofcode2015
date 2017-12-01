import re


def has_three_vowels(string):
    res = re.findall(r"[aeiou]",string)
    if len(res) >= 3:
        return True
    else:
        return False


def has_double_letter(string):
    res = re.search(r"(\w)\1",string)
    if res:
        return True
    else:
        return False


def has_not_ugly(string):
    res = re.search(r"ab|cd|pq|xy",string)
    if res:
        return False
    else:
        return True


def has_double_that_repeat(string):
    res = re.search(r"(\w{2}).*\1",string)
    if res:
        return True
    else:
        return False


def has_repeat_between(string):
    res = re.search(r"(\w).\1", string)
    if res:
        return True
    else:
        return False


if __name__ == '__main__':
    nb_nice = 0
    with open("input","r") as f:
        for line in f:
            if has_three_vowels(line) and has_double_letter(line) and has_not_ugly(line):
                nb_nice += 1
    print("part1 nb_nice :",nb_nice)

    nb_nice = 0
    with open("input","r") as f:
        for line in f:
            if has_double_that_repeat(line) and has_repeat_between(line):
                nb_nice += 1
    print("part2 nb_nice :",nb_nice)