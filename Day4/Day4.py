import hashlib

secret_key='yzbqklnj'

def test_if_5zeros(string):
    m = hashlib.md5()
    string_to_hash = string.encode('utf-8')
    m.update(string_to_hash)
    if m.hexdigest()[0:5] == "00000":
        print(string)
        print(m.hexdigest())
        return True
    else:
        return False


def test_if_6zeros(string):
    m = hashlib.md5()
    string_to_hash = string.encode('utf-8')
    m.update(string_to_hash)
    if m.hexdigest()[0:6] == "000000":
        print(string)
        print(m.hexdigest())
        return True
    else:
        return False


if __name__ == '__main__':
    i=0
    while not test_if_5zeros(secret_key+str(i)) :
        i=i+1
    print(i)
    print("Now 6 zeros !")
    while not test_if_6zeros(secret_key + str(i)):
        i = i + 1
    print(i)
