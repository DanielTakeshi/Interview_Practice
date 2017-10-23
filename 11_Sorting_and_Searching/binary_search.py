""" This should work. """

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


if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(data, 0))
    print(binary_search(data, 1))
    print(binary_search(data, 2))
    print(binary_search(data, 8))
    print(binary_search(data, 9))
    print(binary_search(data, 10))
    print(binary_search(data, 11))
    print("")

    data = [1]
    print(binary_search(data, 0))
    print(binary_search(data, 1))
    print(binary_search(data, 2))
    print("")

    data = [1,2]
    print(binary_search(data, 0))
    print(binary_search(data, 1))
    print(binary_search(data, 2))
    print(binary_search(data, 3))
    print("")
