"""  My attempt at answering question 6, in 2017. """

from stack_queue import Stack
import numpy as np

def sort_stack(s):
    assert not s.is_empty()
    ss = Stack() # This will be the auxiliary stack
        
    num_elements = 0
    while not s.is_empty():
        ss.push( s.pop() )
        num_elements += 1

    num_sorted = 0
    while num_sorted < num_elements:
        # `num_sorted` is how much `s` is filled.
        # `ss` has the `num_elements-num_sorted` elements.
        min_item = np.float('inf')

        # Search through all non-sorted items to find minimum.
        for _ in range(num_elements-num_sorted):
            item = ss.pop()
            if item < min_item:
                min_item = item
            s.push(item)

        # Put all unsorted items other than the one with min back
        # into ss, if we get the min hold it out and put it in s.
        got_min = False # Handle duplicates

        for _ in range(num_elements-num_sorted):
            item = s.pop()
            if item == min_item and not got_min:
                got_min = True
            else:
                ss.push(item)
        s.push(min_item)
        num_sorted += 1

    return s   


if __name__ == "__main__":
    lists = [
        [1,2,3],
        [3,2,1],
        [2,5,4,6,7,3,4,9,1,1,0,-1,44]
    ]
    for l in lists:
        s = Stack()
        for item in l:
            s.push(item)
        print("\nSorting: {}".format(s))
        print("Result:  {}".format(sort_stack(s)))
