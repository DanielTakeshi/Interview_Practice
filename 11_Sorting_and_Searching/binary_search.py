""" This should work. 

Note: if high/end is exclusive, then `mid` rounds UP as needed.
If high/end is inclusive, then `mid `rounds DOWN as needed.
Makes sense, because the exclusive part means we have a higher number that
represents our upper bound.

Either way should work. But stick with inclusive for now.
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



def bsearch_iterative_ex(data, value):
    """ Iterative way, EXCLUSIVE for the high value. """
    if len(data) == 0:
        return -1
    low = 0
    high = len(data)
    while low < high:
        mid = int((low+high)/2) # Rounds up
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            high = mid # We DON'T check `mid` again since high is _exclusive_.
        else:
            low = mid+1
    return -1 

def bsearch_iterative(data, value):
    """ Iterative way, inclusive on both ends. """
    if len(data) == 0:
        return -1
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((low+high)/2) # Rounds down
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            high = mid-1
        else:
            low = mid+1
    return -1 


if __name__ == "__main__":
    methods = [binary_search_ex, binary_search, bsearch_iterative_ex, bsearch_iterative]
    for i,meth in enumerate(methods):
        print("METHOD {}".format(i))
        data = [1,2,3,4,5,6,7,8,9,10]
        print(meth(data, 0))
        print(meth(data, 1))
        print(meth(data, 2))
        print(meth(data, 8))
        print(meth(data, 9))
        print(meth(data, 10))
        print(meth(data, 11))
        print("")

        data = [1]
        print(meth(data, 0))
        print(meth(data, 1))
        print(meth(data, 2))
        print("")

        data = [1,2]
        print(meth(data, 0))
        print(meth(data, 1))
        print(meth(data, 2))
        print(meth(data, 3))
        print("")
