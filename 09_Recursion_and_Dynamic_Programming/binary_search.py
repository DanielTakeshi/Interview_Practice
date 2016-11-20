"""
Binary search practice. Here, we look for an element x in a SORTED array, called
... 'array'. Be sure to get the edge cases correct.  I think  the easiest thing
for me to remember in the future is to always have the "high" indices be
**inclusive**, not exclusive. And to ALWAYS have mid = (low + high)/2. Then we
have already tested mid, so we want our updated low or high variable to be ONE
OFF of mid. Not exactly mid.

One can also do this recursively.
"""

def binary_search(array, x):
    low = 0
    high = len(array)-1
    while (low <= high):
        mid = (low+high)/2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            high = mid-1
        else:
            low = mid+1
    return -1

if __name__ == "__main__":
    l1 = [x for x in range(100)]
    print(binary_search(l1, 10))
