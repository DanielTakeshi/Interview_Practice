
def merge(A, B):
    """PROBLEM 01 in CtCI 6th edition.

    In Python we'll assume we can just append to A.
    Should be O(|A|+|B|) time *and* space complexity.
    Simpler way is to concatenate empty stuff at the beginning but
    the question suggests we should explicitly write the shifting.

    ASSUMES that len(A) >= 1 and len(B) >= 1.
    """
    for _ in range(len(B)):
        A.append('')
    for i in range(len(A)-1, -1, -1):
        A[i] = A[i-len(B)]
        if i-len(B) == 0:
            break
    min_a_idx = len(B)
    min_b_idx = 0

    # There's definitely a cleaner way to do this.
    for i in range(len(A)):
        if min_a_idx < len(A):
            min_a = A[min_a_idx]
        else:
            min_a = B[-1] + 1  # so we never use it.
        if min_b_idx < len(B):
            min_b = B[min_b_idx]
        else:
            min_b = A[-1] + 1 # so we never use it.

        if min_a < min_b:
            A[i] = min_a
            min_a_idx += 1
        else:
            A[i] = min_b
            min_b_idx += 1
    return A


if __name__ == "__main__":
    # ----------------- Problem 01 ----------------
    print('-'*120)
    print('ON PROBLEM NUMBER ONE')
    print('-'*120)
    arrays = [
        ([1,2,3], [1]),
        ([1,2,3], [1,2,3]),
        ([1,2,3], [4,5,6]),
        ([4,5,6], [1,2]),
    ]
    for array_tuple in arrays:
        A, B = array_tuple
        print('\nOn the following arrays for (A,B): {}'.format(array_tuple))
        res = merge(A, B)
        print('result:  {}'.format(res))
    print()
