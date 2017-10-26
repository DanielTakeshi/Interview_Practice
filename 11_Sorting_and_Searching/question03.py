"""
Question 11.3 practice.
"""

def binary_search(x, array):
    low = 0
    high = len(array)-1
    while (low <= high):
        mid = int( (low+high)/2 )
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            high = mid-1
        else:
            low = mid+1
    return -1

# 2016
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
        mid = int( (high+low)/2 )
        if rot_list[mid-1] > rot_list[mid]:
            cutoff = mid
            break
        elif rot_list[0] > rot_list[mid]:
            high = mid
        else: 
            low = mid

    print("pivot: {}".format(cutoff))
    # Then run binary search on the cutoff points with offset as needed!
    if item < rot_list[0]:
        val = binary_search(item, rot_list[cutoff:])
        if val == -1:
            return -1
        else:
            return val + cutoff
    else:
        return binary_search(item, rot_list[:cutoff])


# 2017
def find_pivot(arr):
    """ Returns **index** in `arr` of the **smallest** element. """
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr)
                        
    # Already sorted case, might be able to remove this later
    if arr[0] < arr[-1] or len(arr) == 1:
        return 0

    while low < high:
        mid = int( (low+high)/2 )
        # This is the pivot point
        if arr[mid] < arr[mid-1]:
            return mid

        # I think this handles duplicates ... really annoyihng due to the case
        # e.g. [3,3,3,1,3].
        if arr[low] == arr[mid] == arr[-1]:
            pivot_left = find_pivot(arr[:mid])
            pivot_right = find_pivot(arr[mid:])
            if pivot_left == -1 or pivot_left == 0:
                return pivot_right + mid
            elif pivot_right == -1 or pivot_right == 0:
                return pivot_left
            else:
                return -1
        elif arr[mid] <= arr[-1]:
            high = mid
        else:
            low = mid+1
    return -1


def find_element(n, arr):
    """ Assume I use my previous binary search code. """
    pivot = find_pivot(arr)
    print("pivot: {}".format(pivot))
    print("binary search on: {}".format(arr[pivot:]+arr[:pivot]))
    index = binary_search(n, arr[pivot:]+arr[:pivot])
    return (index + pivot) % len(arr)


if __name__ == "__main__":
    print(find_in_rotated(1, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 5
    print(find_element(1, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 5
    print("")
    print(find_in_rotated(2, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be -1
    print(find_element(2, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be -1
    print("")
    print(find_in_rotated(3, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 6
    print(find_element(3, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 6
    print("")
    print(find_in_rotated(4, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 7
    print(find_element(4, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 7
    print("")
    print(find_in_rotated(5, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 8
    print(find_element(5, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 8
    print("")
    print(find_in_rotated(7, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 9
    print(find_element(7, [15,16,19,20,25,1,3,4,5,7,10,14])) # Should be 9
    print("")
    print(find_in_rotated(3, [2,3,4,4,4,2,2])) # 1
    print(find_element(3, [2,3,4,4,4,2,2])) # 1
    print("")
    print(find_in_rotated(1, [3,3,3,1,3])) # 3
    print(find_element(1, [3,3,3,1,3])) # 3
    print("")
    print(find_in_rotated(4, [2,2,2,3,4,2])) # 4
    print(find_element(4, [2,2,2,3,4,2])) # 4
