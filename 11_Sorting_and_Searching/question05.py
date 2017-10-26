""" Question 11.5 practice. """

def find_loc_recursive(arr, s, low, high):
    if len(s) == 0 or low > high:
        return -1
    mid = int( (low+high)/2 )
    if arr[mid] == s:
        return mid
    elif arr[mid] == "":
        # special case introduced by the problem
        # must check both recursive branches.
        l_ind = find_loc_recursive(arr, s, low, mid-1)
        r_ind = find_loc_recursive(arr, s, mid+1, high)
        if l_ind != -1:
            return l_ind
        elif r_ind != -1:
            return r_ind
        else: 
            return -1
    elif arr[mid] < s:
        # search to the right in the array
        return find_loc_recursive(arr, s, mid+1, high)
    else:
        # search to the left in the array
        return find_loc_recursive(arr, s, low, mid-1)


def find_loc(arr, s):
    """
    Assumes `s` consists of 26 characters for simplicity. 
    This also means we can use Python's < and >. Easy.
    """
    return find_loc_recursive(arr, s, low=0, high=len(arr)-1)


if __name__ == "__main__":
    arrays = [
        (["a","","","b"], "a"),
        (["at","","","","ball","","","car","","","dad","",""], "at"),
        (["at","","","","ball","","","car","","","dad","",""], "ball"),
        (["at","","","","ball","","","car","","","dad","",""], "car"),
        (["at","","","","ball","","","car","","","dad","",""], "dad")
    ]
    
    for arr,string in arrays:
        print("\nfor array {} ...\n{} has index {}".format(arr, string, find_loc(arr, string)))
