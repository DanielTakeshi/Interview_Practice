""" For 2016 ... """

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


def problem_04(str_input, str_length=None):
    """ Assumes that str_input is a string.  A bit silly since we ignore
    str_length but there's some ambiguity with the question, I think. 
    """
    str_split = str_input.split()
    res = ""
    for ch in str_split[:-1]:
        res += ch + "%20"
    res += str_split[-1]
    return res


def problem_05(word):
    """ This should work, ironically very similar to Gayle's slow code.
    
    But I'll try and figure out how to do it using the Python version of string
    buffers. Lots of work for me to do ...
    """
    compressed = ""
    total = 1
    prev_ch = word[0]

    for (idx,ch) in enumerate(word[1:]):
        if ch == prev_ch:
            total += 1
        else:
            compressed += prev_ch + str(total)
            total = 1
            prev_ch = ch
        if len(word)-2 == idx:
            compressed += ch + str(total)

    if len(compressed) < len(word):
        return compressed
    else:
        return word


def problem_06():
    pass


def problem_07(mat):
    """ Uses numpy, assumes 'mat' is (m,n) numpy array. """
    nrows,ncols = mat.shape
    mat_copy = np.copy(mat)

    for i in range(nrows):
        for j in range(ncols):
            if (mat[i,j] == 0):
                # Use broadcast, then skip this row.
                mat_copy[i,:] = 0
                mat_copy[:,j] = 0
    return mat_copy


def problem_08():
    pass


if __name__ == "__main__":
    a = np.ones((4,4))
    a[3,1] = 0
    a[3,0] = 0
    print(a)
    print(problem_07(a))
