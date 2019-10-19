""" I didn't do this in 2016. """

def check_list_sum(plist):
    """ Assumes plist is a list of -1s and 1s. """
    return sum([int(p) for p in plist])

def get_parens(n):
    paths = [['+1']] # List of lists of matching parentheses.

    for i in range(1,2*n):
        old_paths = list(paths)
        new_paths = []

        for path in old_paths:
            new_path1 = list(path)
            new_path2 = list(path)
            new_path1.append('-1')
            new_path2.append('+1')
            if check_list_sum(new_path1) >= 0: 
                new_paths.append( new_path1)
            if check_list_sum(new_path2) >= 0:
                new_paths.append( new_path2)

        # Now get `paths` updated.
        paths = list(new_paths)

    # Ignore anything which doesn't sum to zero.
    return [p for p in paths if check_list_sum(p) == 0]

def pretty_string_parens(items):
    """ Assumes items has 1s and -1s. """
    string = ""
    for ii in items:
        paren = "(" if ii == '+1' else ")" 
        string += paren
    return string

def print_parens(n):
    assert n >= 0
    if n == 0:
        print("")
    else:
        parens = get_parens(n)
        for item in parens:
            print(pretty_string_parens(item))

if __name__ == "__main__":
    for i in range(5):
        print("\n\nNOW PRINTING FOR {} _PAIRS_ OF PARENTHESES:".format(i))
        print_parens(i)
