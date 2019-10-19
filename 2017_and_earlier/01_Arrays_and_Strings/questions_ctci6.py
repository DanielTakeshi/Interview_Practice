""" 
In the 2016 edition, there were two additional questions that I hadn't tried.
"""

def is_palindrome_of_permutation(s):
    """ O(n^2) solution. """
    s = s.replace(' ', '') # I think this strips whitespaces...
    s = s.lower()
    max_odd = len(s) % 2
    num_odd = 0

    for char in s:
        if s.count(char) % 2 == 1:
            num_odd += 1
            if num_odd > max_odd:
                return False
    return True


def is_palindrome_of_permutation_v2(s):
    """ O(n log n) solution due to sorting first. """
    s = s.replace(' ', '')
    s = s.lower()
    s = "".join(sorted(s))
    max_odd = len(s) % 2
    num_odd = 0
    num_same = 0
    prev_char = "aa" # Different from all chars since it's 2 chars :)
    
    for char in s:
        if char == prev_char:
            num_same += 1
        else:
            if num_same % 2 == 1:
                num_odd += 1
                if num_odd > max_odd:
                    return False
            num_same = 1
            prev_char = char

    return True


def at_most_one_edit(s1, s2):
    if s1 == s2:
        return True
    diff = abs(len(s1) - len(s2))

    if diff >= 2:
        return False
    elif diff == 1:
        # We must insert a character in the shorter string
        if len(s1) < len(s2):
            return check_insertion(s1, s2)
        else:
            return check_insertion(s2, s1)
    else:
        # We know this is a replacement.
        num_replace_char = 0
        for ch1,ch2 in zip(s1,s2):
            if ch1 != ch2:
                num_replace_char += 1
        return num_replace_char <= 1


def check_insertion(s1, s2):
    assert len(s1) < len(s2)
    s2index = 0
    for ch in s1:
        if ch != s2[s2index]: 
            s2index += 1
            if len(s2) <= s2index or ch != s2[s2index]:
                return False # Can't have two consecutive fails
        s2index += 1
    return True


if __name__ == "__main__":
    print("\nProblem 4 in CtCI 6th edition.")
    print(is_palindrome_of_permutation('T')) # True
    print(is_palindrome_of_permutation('Tt')) # True
    print(is_palindrome_of_permutation('Ttf')) # True
    print(is_palindrome_of_permutation('Ttfa')) # False
    print(is_palindrome_of_permutation('Tact Coa')) # True
    print("")
    print(is_palindrome_of_permutation_v2('T')) # True
    print(is_palindrome_of_permutation_v2('Tt')) # True
    print(is_palindrome_of_permutation_v2('Ttf')) # True
    print(is_palindrome_of_permutation_v2('Ttfa')) # False
    print(is_palindrome_of_permutation_v2('Tact Coa')) # True

    print("\nProblem 5 in CtCI 6th edition.")
    print(at_most_one_edit('pale','ple')) # True
    print(at_most_one_edit('pales','pale')) # True
    print(at_most_one_edit('pale','bale')) # True
    print(at_most_one_edit('pale','bake')) # False
