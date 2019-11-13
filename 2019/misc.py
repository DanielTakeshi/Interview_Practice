

def compare(a,b):
    return max(a,b)


def _second_max(arr):
    """Definitely O(n) time, O(1) extra space.

    But is it the *minimum* amount of times we call `compare()`? Best
    case scenario, if we keep having larger and larger elements, i.e.,
    array is sorted in increasing order, we call `compare` exactly
    n-1 times. Worst case, if we always go to second, it's 2n-1 times.

    Actually if we assume a randomly scrambed array, then it's very
    likely that we will NOT exceed a second max, so we should arguably
    do the second max comparison first, if second max comparison yields
    the second max, then we are done.

    This should also appropriately handle duplicate items.
    """
    if len(arr) <= 1:
        raise ValueError(arr)

    # Handle the base case.
    if compare(arr[0], arr[1]) == arr[0]:
        first_max = arr[0]
        second_max = arr[1]
    else:
        first_max = arr[1]
        second_max = arr[0]

    for i in range(2, len(arr)):
        if compare(first_max, arr[i]) == arr[i]:
            second_max = first_max
            first_max = arr[i]
        else:
            # Don't change first_max, but may have to change a second.
            if compare(second_max, arr[i]) == arr[i]:
                second_max = arr[i]
    return second_max


if __name__ == "__main__":
    # Hmm ... seems to be passing!
    lists = [
        [1,2],
        [2,2],
        [2,2,3,4,5,6,5,6,7],
        [8,2,3,4,5,6,5,6,7],
        [8,9,3,4,5,6,5,6,7],
        [1,1,1,1,1],
    ]
    for l in lists:
        print('second_max: {}, from {}'.format(_second_max(l), l))
