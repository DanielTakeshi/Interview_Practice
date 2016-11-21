""" 
Question 9.5 practice 

I think this works. If you notice, all the 'items' are strings, so when I do
item[:i] or item[:i], I get strings back, so I have to encode them into lists
before I can do the list concatenation.
"""

import copy

def get_permutations(s):
    """ Assumes that s has unique characters. """
    if len(s) == 1:
        return [s]
    other_permutations = get_permutations(s[:-1])
    new_permutations = []
    for item in other_permutations:
        for i in range(len(s)):
            before = [item[:i]]
            after = [item[i:]]
            new_perm = "".join(before + [s[-1]] + after)
            new_permutations.append( new_perm )
    return new_permutations

if __name__ == "__main__":
    print(get_permutations("a"))
    print(get_permutations("ab"))
    print(get_permutations("abc"))
    print(get_permutations("abcd"))
    print(get_permutations("abcde"))
