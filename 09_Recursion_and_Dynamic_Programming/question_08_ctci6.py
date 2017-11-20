""" Question 8 from the 6th edition, the permutations with duplicates. """

import copy

# Global variable.
all_permutations = []

def permutations_with_dups(s):
    """ Returns a list of all unique permutations of string s. """
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    current_perm = ""
    permutations(counts, current_perm)
    return all_permutations


def permutations(counts, current_perm):
    """
    counts: dict used to get char counts from full string
    current_perm: string representing the permutation _prefix_.
    """
    if exit(counts):
        all_permutations.append(current_perm)

    for ch in counts:
        if counts[ch] == 0:
            continue
        new_counts = copy.copy(counts)
        new_counts[ch] -= 1
        new_perm_prefix = current_perm + ch
        permutations(new_counts, new_perm_prefix)


def exit(d):
    """ d is a dict """
    for key in d:
        if d[key] != 0:
            return False
    return True


if __name__ == "__main__":
    strings = ["a",
               "aa",
               "aab",
               "aaab",
               "aaabbc"]
    for string in strings:
        print("\nTesting permutations with string: {}".format(string))
        perms = permutations_with_dups(string)
        all_permutations = []
        for p in perms:
            print(p)
        print("(number of permutations: {})".format(len(perms)))
