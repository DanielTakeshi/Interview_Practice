"""Modified from my 2017 solutions, with some more testing.

- If high/end is exclusive, then `mid` rounds UP as needed.
- If high/end is inclusive, then `mid `rounds DOWN as needed.

Either way should work. It is probably best to stick with one of the inclusive
or exclusive ways. There are also recursive and iterative solutions.

I'm also adding a special case, to return the index we WOULD be inserting the
target value in, if we wanted to do that!
"""

def binary_search_ex(data, value):
    """ Recursive method, exclusive for the high. """
    return bsearch_ex(data, value, start=0, end=len(data))

def bsearch_ex(data, value, start, end):
    if start >= end:
        return -1
    mid = int((start+end)/2)
    if data[mid] == value:
        return mid
    elif data[mid] > value:
        return bsearch_ex(data, value, start=start, end=mid)
    else:
        return bsearch_ex(data, value, start=mid+1, end=end)

def binary_search(data, value):
    """ Recursive method, inclusive. """
    return bsearch(data, value, start=0, end=len(data)-1)

def bsearch(data, value, start, end):
    if start > end:
        return -1
    mid = int((start+end)/2)
    if data[mid] == value:
        return mid
    elif data[mid] > value:
        return bsearch(data, value, start=start, end=mid-1)
    else:
        return bsearch(data, value, start=mid+1, end=end)

def bsearch_iterative_ex(data, value, return_targ_if_missing=True):
    """Iterative way, EXCLUSIVE for the high value.

    While loop conditions on low<high, because if low==high then we are done,
    high is exclusive so we can't possibly be searching at int((low+high)/2).
    """
    if len(data) == 0:
        return -1
    low = 0
    high = len(data)
    while low < high:
        mid = int((low+high)/2)
        if data[mid] < value:
            low = mid+1
        elif data[mid] > value:
            high = mid
        else:
            return mid
    if return_targ_if_missing:
        # Where the index would be if we wanted to insert into it.
        assert low == high
        return low
    else:
        return -1

def bsearch_iterative_in(data, value, return_targ_if_missing=True):
    """Iterative way, inclusive on both ends.

    While loop has to handle the low==high case because high is inclusive, so
    we may still need to check at index int((low+high)/2). This solution is
    pretty much an exact match with Gayle's iterative solution (Chapter 10).
    """
    if len(data) == 0:
        return -1
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((low+high)/2)
        if data[mid] < value:
            low = mid+1
        elif data[mid] > value:
            high = mid-1
        else:
            return mid
    if return_targ_if_missing:
        # Where the index would be if we wanted to insert into it.
        # Trickier than the previous case, but we want the index at
        # low+1, since if high were exclusive, it wouldd be higher.
        assert low-1 == high, '(low,high): ({},{})'.format(low,high)
        return low
    else:
        return -1


if __name__ == "__main__":
    #methods = [binary_search_ex, binary_search, bsearch_iterative_ex, bsearch_iterative]
    methods = [bsearch_iterative_ex, bsearch_iterative_in]
    print('NOTE! Watch out if return_targ_if_missing=True !!')

    for i,meth in enumerate(methods):
        data = [1,2,3,4,5,6,7,8,9,10]
        print('')
        print('-'*100)
        print("BINARY SEARCH METHOD {}".format(i))
        print('(target_value, index_in_data)')
        print('-'*100)
        print("\nNow data: {}".format(data))
        print('{}:\t {}'.format(0,  meth(data, 0)))
        print('{}:\t {}'.format(1,  meth(data, 1)))
        print('{}:\t {}'.format(2,  meth(data, 2)))
        print('{}:\t {}'.format(8,  meth(data, 8)))
        print('{}:\t {}'.format(9,  meth(data, 9)))
        print('{}:\t {}'.format(10, meth(data, 10)))
        print('{}:\t {}'.format(11, meth(data, 11)))

        data = [11,22,33,44,55,66,77,88,99]
        print("\nNow data: {}".format(data))
        print('{}:\t {}'.format(10,  meth(data, 10)))
        print('{}:\t {}'.format(11,  meth(data, 11)))
        print('{}:\t {}'.format(12,  meth(data, 12)))
        print('{}:\t {}'.format(21,  meth(data, 21)))
        print('{}:\t {}'.format(23,  meth(data, 23)))

        data = [1]
        print("\nNow data: {}".format(data))
        print('{}:\t {}'.format(0, meth(data, 0)))
        print('{}:\t {}'.format(1, meth(data, 1)))
        print('{}:\t {}'.format(2, meth(data, 2)))

        data = [1,2]
        print("\nNow data: {}".format(data))
        print('{}:\t {}'.format(0, meth(data, 0)))
        print('{}:\t {}'.format(1, meth(data, 1)))
        print('{}:\t {}'.format(2, meth(data, 2)))
