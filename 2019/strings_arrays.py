## ------------------------ PROBLEM 01 ------------------------ ##
## ------------------------ PROBLEM 02 ------------------------ ##
## ------------------------ PROBLEM 03 ------------------------ ##

def urlify(s, slen):
    """Assumes we ignore whitespace at the end.

    The easy python way of doing it, but if we want to assume a fixed array
    with the space to include the string … and to do the operation in place …
    then lets make a new method.
    """
    assert slen >= 1
    s = s.rstrip() # remove whitespace
    replacement = '%20'
    new_s = s.replace(' ', replacement)
    return new_s


def urlify_inplace(s, slen):
    """Should be done in-place.

    Here the question seems to want to define s as some fixed length
    array, with sufficient space at the end to do the operation in place.
    Assume we can get rid of whitespace at the end.  Here O(N) time (N=string
    length), O(1) extra space.
    """
    assert slen >= 1

    # We assume `s` is a string so let's just expand it into a list
    # and pretend that is the input.
    s = s.rstrip()
    s_arr = [ch for ch in s]
    for ch in s:
        if ch == ' ':
            s_arr.append(' ')
            s_arr.append(' ')

    # Now we have s_arr with the original string, WITH enough space at the end
    # to include all the characters with the %20 replacement.  So now we are
    # matching the problem assumption.  Go IN REVERSE, and we are not at risk
    # of over-riding chars. Assume slen-1 points to the index of the last char
    # (which is not a space because we trim it).

    c = slen - 1             # go through chars in original string
    i = len(s_arr) - 1       # go through index of new string

    while i >= 0:
        if s_arr[c] == ' ':
            s_arr[i] = '0'
            s_arr[i-1] = '2'
            s_arr[i-2] = '%'
            i -= 3
        else:
            s_arr[i] = s_arr[c]
            i -= 1
        c -= 1
        assert i >= c

    # join into a new string
    return ''.join(s_arr)


def test01():
    return 'k '

def test02():
    return 'Mr John Smith'

def test03():
    return 'Mr John Smith   '

def test04():
    return 'blahBlah'

def test05():
    return 'blah B l  a'

def test06():
    return ' x '

def test07():
    return '  x  x'


## ------------------------ PROBLEM 04 ------------------------ ##

def is_palind_perm(s):
    # case insensitive by problem assumption
    # also spaces do NOT count
    s = s.lower()
    s = s.replace(' ','')

    # Iterate through char, put in dict (w/hash table) so O(N) time/space.
    char_counts = {}
    for ch in s:
        if ch not in char_counts:
            char_counts[ch] = 1
        else:
            char_counts[ch] += 1

    # tally up counts.
    nb_odd_counts = 0
    for ch in char_counts:
        if char_counts[ch] % 2 != 0:
            nb_odd_counts += 1
        if nb_odd_counts > 1:
            return False

    if len(s) % 2 == 0:
        return nb_odd_counts == 0
    else:
        return nb_odd_counts == 1


## ------------------------ PROBLEM 05 ------------------------ ##
## ------------------------ PROBLEM 06 ------------------------ ##
## ------------------------ PROBLEM 07 ------------------------ ##
## ------------------------ PROBLEM 08 ------------------------ ##
## ------------------------ PROBLEM 09 ------------------------ ##



if __name__ == "__main__":
    # ----------------- Problem 03 (v1) ----------------
    print('')
    print('-'*120)
    print('PROBLEM 3, FIRST VERSION\n')
    strings = [test01(), test02(), test03(), test04(), test05(), test06(), test07()]
    for s in strings:
        print('Before: {}'.format(s))
        s = urlify(s, slen=len(s.rstrip()))
        print('After:  {}\n'.format(s))

    # ----------------- Problem 03 (v2) ----------------
    print('')
    print('-'*120)
    print('PROBLEM 3, SECOND VERSION\n')
    strings = [test01(), test02(), test03(), test04(), test05(), test06(), test07()]
    for s in strings:
        print('Before: {}'.format(s))
        s = urlify_inplace(s, slen=len(s.rstrip()))
        print('After:  {}\n'.format(s))

    # ----------------- Problem 04 ----------------
    print('')
    print('-'*120)
    print('PROBLEM 4, SECOND VERSION\n')
    strings = ['a', 'aa', 'aaa', ' a', 'aba', 'ab', 'Tact Coa', 'tactcoapapa',
                'tactcoapapaa', 'aaaab', 'aaaabb', 'aaaabc']
    for s in strings:
        print('is_palind_perm: {}  for:  {}'.format(is_palind_perm(s), s))
