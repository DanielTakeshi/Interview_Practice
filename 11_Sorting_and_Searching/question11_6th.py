""" Testing Question 10.11, peaks and valleys. """

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def peaks_and_valleys(arr):
    """ For now, return a peak first, then valley, etc. """
    if len(arr) <= 1:
        return arr

    # Enforce that `insert_idx` is the stuff we'll insert next.
    insert_idx = 0
    res = []
    type = 1  # 1 = peak, -1 = valley

    while insert_idx+1 < len(arr):
        # If type == 1, want `arr[insert_idx]` to be a peak.
        # If type == -1, want `arr[insert_idx]` to be a valley.
        if type == 1:
            if arr[insert_idx] < arr[insert_idx+1]:
                swap(arr, insert_idx, insert_idx+1)
        else:
            if arr[insert_idx] > arr[insert_idx+1]:
                swap(arr, insert_idx, insert_idx+1)
        res.append(arr[insert_idx])
        insert_idx += 1
        type *= -1

    # Last index should be correct by construction.
    res.append(arr[insert_idx]) 
    return res


if  __name__ == "__main__":
    arrays = [
        [1,2],
        [2,1],
        [2,2],
        [5,3,1,2,3],
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9],
    ]
    for arr in arrays:
        arr_copy = list(arr)
        p_and_v = peaks_and_valleys(arr)
        print("  original: {}\n  p_and_v:  {}\n".format(arr_copy, p_and_v))
