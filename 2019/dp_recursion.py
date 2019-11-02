## ------------------------ PROBLEM 01 ------------------------ ##

def possible_ways(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    ways = [0, 1, 2, 4]
    for k in range(4, n+1):
        ways.append( ways[k-1] + ways[k-2] + ways[k-3] )
    return ways[-1]


## ------------------------ PROBLEM 02 ------------------------ ##
## ------------------------ PROBLEM 03 ------------------------ ##
## ------------------------ PROBLEM 04 ------------------------ ##

def power_set(data):
    """Assume `data` is a python LIST to allow for indexing."""
    if len(data) == 0:
        print(set())
    else:
        get_sets(data, current_set=set(), index=0)

import copy

# printing sets
def get_sets(data, current_set, index):
    set0 = copy.copy(current_set)
    current_set.add( data[index] )
    set1 = copy.copy(current_set)
    new_index = index + 1
    if new_index < len(data):
        get_sets(data, set0, new_index)
        get_sets(data, set1, new_index)
    else:
        print(set0)
        print(set1)


def get_sets_list(data, index):
    if len(data) == index:
        all_subsets = [ [] ]
    else:
        all_subsets = get_sets_list(data, index+1)
        item = data[index]
        new_subsets = []
        for subset in all_subsets:
            new_subset = []
            new_subset.extend(subset)
            new_subset.append(item)
            new_subsets.append(new_subset)
        for ss in new_subsets:
            all_subsets.append(ss)
    return all_subsets


## ------------------------ PROBLEM 05 ------------------------ ##
## ------------------------ PROBLEM 06 ------------------------ ##
## ------------------------ PROBLEM 07 ------------------------ ##
## ------------------------ PROBLEM 08 ------------------------ ##
## ------------------------ PROBLEM 09 ------------------------ ##



if __name__ == "__main__":
    # ----------------- Problem 01 ----------------
    print('')
    print('-'*120)
    print('PROBLEM 1, FIRST VERSION\n')
    for n in range(38):
        print('For n={}, ways: {}'.format(str(n).zfill(3), possible_ways(n)))

    # ----------------- Problem 04 ----------------
    print('')
    print('-'*120)
    print('PROBLEM 4, FIRST VERSION\n')
    test_lists = [
        [],
        ['a'],
        ['a','b'],
        ['a','b','c'],
        ['a','b','c','d'],
    ]

    # If we are just printing:
    for items_list in test_lists:
        print('\nFor: {}, the power set contains:'.format(items_list))
        power_set(items_list)

    # If we are just printing:
    for items_list in test_lists:
        print('\nFor: {}, the power set contains:'.format(items_list))
        all_subsets = get_sets_list(items_list, index=0)
        for a in all_subsets:
            print(a)
