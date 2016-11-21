"""
Question 11.3 practice.
"""

def binary_search(x, array):
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

def find_in_rotated(item, rot_list):
    """ Strategy: do binary search to find the rotation point.  Then do a second
    search within a sorted array.  For now, assume list has length >= 2 (if 1
    it's trivial...). 
    """

    # First case: the rot_list is actually ordered.
    if rot_list[0] < rot_list[-1]:
        return binary_search(item, rot_list)

    # Otherwise, find the cutoff point.
    low = 0
    high = len(rot_list) # I think this may be needed ... so no -1 here ...
    cutoff = -1 # The first index of the second sorted array.

    while (low <= high):
        mid = (high+low)/2
        if rot_list[mid-1] > rot_list[mid]:
            cutoff = mid
            break
        elif rot_list[0] > rot_list[mid]:
            high = mid
        else: 
            low = mid

    # Then run binary search on the cutoff points with offset as needed!
    if item < rot_list[0]:
        val = binary_search(item, rot_list[cutoff:])
        if val == -1:
            return -1
        else:
            return val + cutoff
    else:
        return binary_search(item, rot_list[:cutoff])

if __name__ == "__main__":
    print(find_in_rotated(1, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 5
    print(find_in_rotated(2, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be -1
    print(find_in_rotated(3, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 6
    print(find_in_rotated(4, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 7
    print(find_in_rotated(5, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 8
    print(find_in_rotated(7, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 9
    # I ran a numbe of tests and it seems to pass. Probably be careful on this!
    print(find_in_rotated(3, [2,3,4,4,4,2,2]))
