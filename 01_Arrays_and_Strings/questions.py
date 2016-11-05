import numpy as np

def joel_spolsky(str_):
    # String starts with upper case letters.
    return str_[0].isupper()

def problem_01(str_input):
    # return len(str_input) == len(set(str_input))
    # Alternative:
    for c in str_input:
        if str_input.count(c) > 1:
            return False
    return True

def problem_01_v1(str_input):
    # Better but numpy is not needed!
    return len(str_input) == len(np.unique( list(str_input) ))

def problem_01_v2(str_input):
    # Terrible version.
    char_dict = {}
    for c in str_input:
        if c in char_dict:
            return False
        char_dict[c] = 1
    return True


def problem_02(str_):
    """ Not sure if Python has null character... """
    return str_[::-1]

def problem_02_v1(str_):
    rev = ""
    for i in range(len(str_)-1, -1, -1):
        rev += str_[i]
    return rev


def problem_03(s1, s2):
    """ Lots of special cases here ..."""
    # I think: return sorted(s1) == sorted(s2) also works
    ch_1 = set(s1)
    ch_2 = set(s2)
    if len(ch_1) != len(ch_2):
        return False
    for c in ch_1:
        if s1.count(c) != s2.count(c):
            return False
    return True


def problem_04():
    print("Not yet implemented")


def problem_05():
    print("Not yet implemented")


def problem_06():
    print("Not yet implemented")


def problem_07():
    print("Not yet implemented")


def problem_08():
    print("Not yet implemented")


if __name__ == "__main__":
    print(problem_03("h", "h"))
    print(problem_03("no", "on"))
    print(problem_03("non", "on"))
    print(problem_03("aaab", "abaa"))
