""" This should work. 

Note: if high/end is exclusive, then `mid` rounds up as needed.
If high/end is inclusive, then `mid `rounds down as needed.

Either way should work.
"""


# Recursive method, exclusive.
def binary_search(data, value):
    return bsearch(data, value, start=0, end=len(data))

def bsearch(data, value, start, end):
    if start >= end:
        return -1
    mid = int((start+end)/2)
    if data[mid] == value:
        return mid
    elif data[mid] > value:
        return bsearch(data, value, start=start, end=mid)
    else:
        return bsearch(data, value, start=mid+1, end=end)

def bsearch_iterative(data, value):
    """ Iterative way, inclusive on both ends. """
    if len(data) == 0:
        return -1
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((low+high)/2)
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            high = mid-1
        else:
            low = mid+1
    return -1 

if __name__ == "__main__":
    methods = [binary_search, bsearch_iterative]
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
