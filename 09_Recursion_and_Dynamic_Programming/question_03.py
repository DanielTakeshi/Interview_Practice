
def magic_fast(array, start, end):
    if end<start or start<0 or end>=len(array):
        return -1
    mid = (start+end)/2
    if (array[mid] == mid):
        return mid
    elif (array[mid] > mid):
        return magic_fast(array, start, mid-1)
    else:
        return magic_fast(array, mid+1, end)

def question_03(array):
    return magic_fast(array, 0, len(array)-1)

if __name__ == "__main__":
    print(question_03([0,2,3,4,5,6,7]))
    print(question_03([-8,0,2,3,4,5,6,7]))
    print(question_03([-8,0,4,8]))
