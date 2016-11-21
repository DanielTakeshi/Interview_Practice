"""
Testing Question 11.2
"""

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        unique_letters = set(s1)
        for letter in unique_letters:
            if s1.count(letter) != s2.count(letter):
                return False
        return True

def sort_set_anagrams(list_str):
    """ Optional challenge: in-place sort. """
    i = 0
    while (i < len(list_str)):
        # Here, i represents the index of a new possible set of anagrams
        s1 = list_str[i]
        num_anagrams = 1
        for j in range(i+1,len(list_str)):
            s2 = list_str[j]

            # If we have anagrams, and indices aren't,
            # already sorted, then we will swap strings.
            if are_anagrams(s1, s2):
                if (j != i+num_anagrams):
                    tmp = list_str[i+num_anagrams]
                    list_str[i+num_anagrams] = list_str[j]
                    list_str[j] = tmp
                num_anagrams += 1

        i += num_anagrams
    return list_str

if  __name__ == "__main__":
    print(sort_set_anagrams(['ab','ba']))
    print(sort_set_anagrams(['ab','ba','bc']))
    print(sort_set_anagrams(['ab','bc','ba']))
    print(sort_set_anagrams(['ab','bc','ba','cc','bc','ba','dd','cc']))
