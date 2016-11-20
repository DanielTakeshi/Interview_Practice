""" 
Question 9.4 practice 

I think this works.
"""

import copy

def get_subsets(s):
    if len(s) == 0:
        return [set()]
    if len(s) == 1:
        return [s, set()]

    # I **think** we can do this; the idea is to remove arbitrary element.
    # So "s" now has one fewer element, i.e. this change is saved into s.
    # I also **think** we can do set addition here, basically to union them.
    # So make two copies, for one we add 'element', for others we don't.

    element = s.pop()
    other_subsets = get_subsets(s)
    new_set = copy.deepcopy(other_subsets)
    for subset in new_set:
        subset.add(element)
    return other_subsets + new_set


if __name__ == "__main__":
    print(get_subsets({}))
    print(get_subsets({"a"}))
    print(get_subsets({"a", "b"}))
    print(get_subsets({"a", "b", "c"}))
