"""
Testing Question 11.1
"""

def merge(a,b):
    a_ind = len(a)-1
    b_ind = len(b)-1
    for _ in range(len(b)):
        a.append(None)
    new_index = len(a)-1

    while (b_ind >= 0 and a_ind >= 0):
        a_max = a[a_ind]
        b_max = b[b_ind]
        if a_max < b_max:
            a[new_index] = b_max
            b_ind -= 1
        else:
            a[new_index] = a_max
            a_ind -= 1
        new_index -= 1

    while b_ind >= 0:
        a[new_index] = b[b_ind]
        b_ind -= 1
    return a


if __name__ == "__main__":
    print(merge([1,2,3,4,5,6], [1,2,3,4,5,6]))
