
## 2016 version:

def magic_fast(array, start, end):
    if end<start or start<0 or end>=len(array):
        return -1
    #mid = (start+end)/2
    mid = int((start+end)/2) # Python 3 change
    if (array[mid] == mid):
        return mid
    elif (array[mid] > mid):
        return magic_fast(array, start, mid-1)
    else:
        return magic_fast(array, mid+1, end)

def question_03(array):
    return magic_fast(array, 0, len(array)-1)


## 2017 version:

def magic_index(arr):
    return magic(arr, low=0, high=len(arr))

def magic(arr, low, high):
    # low = inclusive bound, high = exclusive bound
    if low >= high:
        return None
    mid = int( (low+high)/2 )
    if arr[mid] > mid: # must "move left"
        return magic(arr, low, mid)
    elif arr[mid] < mid: # must "move right"
        return magic(arr, mid+1, high)
    else: 
        return mid

if __name__ == "__main__":
    lists = [
        [0,2,3,4,5,6,7],
        [-8,0,2,3,4,5,6,7], # Oh this one has multiple magic indices. :-0 Interesting.
        [-8,0,4,8],
        [1,1,1,1] # Tests distinctness. :-)
    ]
    for l in lists:
        print("\nfor list: {}\nwe have 2016 version: {}\n    and 2017 version: {}".format(
                l, question_03(l), magic_index(l)))
