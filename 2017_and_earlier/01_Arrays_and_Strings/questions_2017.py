""" For 2017  ... """

def all_unique_nods(s):
    """ The no data structures version. O(n^2) bleh. 
    
    Alternative is to make an array with length equal to the number of
    characters that are allowed in the input string, but I'm not sure how many
    of those are for Python. And that uses an external data structure ...

    Another option, if I wanted to use sets, is to do `set(s)`. If `s` is a
    string, this WILL split it up in charactesr. If `s` is a list, it just
    splits it up one element for each list element. Man, clever. :-)
    """
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# Based on doing this again, from the sixth edition of CtCI.

def all_unique_6v1(s):
    """ 
    The runtime has to be O(n) here since we need to iterate through all
    characters in the string, and we have no idea if that last character breaks
    the unique-ness property of the other characters.
    """
    return len(set(s)) == len(s)

def all_unique_6v2(s):
    """ 
    Without external data structures.  This is actually O(n^2) I think, as I
    iterate through each character, and then for each, the count method is O(n).
    """
    for char in s:
        if s.count(char) > 1:
            return False
    return True


def reverse(str_):
    """ There are two other ways to do this. 
    
    You can do it incrementally by starting with an empty string and going
    backwards, etc. Unfortunately, that (likely) has to reconstruct the string,
    so it's O(n^2) characters.
    
    The other way is to do the whole tmp = (later index) and then do the
    reassignment swapping, but you can't do that with Python strings.
    
    TBH just remember the slicing thing, it's so much easier.
    """
    return str_[::-1]


def is_permutation(str1, str2):
    """ I think this works! Unfortunately it's O(n^2). Better to sort both of
    the strings and then check sequentially, which is O(n log n). You can also
    do this in a Pythonic way:

        return sorted(str1) == sorted(str2)
        
    Which automatically handles the case of varying string lengths.  But there's
    no way that's O(n).
    """
    if len(str1) != len(str2):
        return False
    for char in str1:
        if str1.count(char) != str2.count(char):
            return False
    return True


def replace_spaces(s, n):
    """ 
    Assumes that s has enough space for the list, so space padded at the end.
    EDIT: yay this was actually what McDowell recommends.
    """
    arr = list(s)
    num_spaces = s[:n].count(' ')
    new = num_spaces*2 + n # exclusive
    old = n-1 # inclusive

    while old >= 0:
        if arr[old] == ' ':
            #arr[new-3] = '%' 
            #arr[new-2] = '2' 
            #arr[new-1] = '0' 
            arr[new-3:new] = ['%','2','0'] # This works ...
            new -= 3
        else:
            arr[new-1] = arr[old]
            new -= 1
        old -= 1

    return "".join(arr[:num_spaces*2+n])


def compress(string):
    """ I think this is cleaner than my 2016 solution. """
    ptr_start = 0
    ptr_end = 0
    num_chars = len(string)
    compressed = []

    while ptr_start < num_chars:
        char = string[ptr_start]
        ptr_end = ptr_start + 1
        while ptr_end < num_chars and string[ptr_end] == char:
            ptr_end += 1
        num_same = ptr_end - ptr_start
        compressed.append( char+str(num_same))
        ptr_start = ptr_end

    compressed_str = "".join(compressed)
    if len(compressed_str) < num_chars:
        return compressed_str
    else:
        return string



def rotate_ninety(image):
    """ Problem 6. Assumes we have a list of lists. 
    
    And I think this works! Bad in terms of space, but whatever ...
    """
    N = len(image)
    assert N == len(image[0])
    rotated = [ [0 for _ in range(N)] for _ in range(N)]
                    
    for row in range(N):
        row_to_copy = image[row]
        col = (N-row) - 1
        for row2 in range(N):
            rotated[row2][col] = row_to_copy[row2]

    return rotated


def clear_rows_cols(matrix):
    """ Yay, Gayle also had two arrays (lists) for the rows and columns to
    clear. :-)

    And she does this the same way I do it ... whew.
    """
    # assumes matrix is a list with M items, each of which is a list of length N
    M = len(matrix)
    N = len(matrix[0])
    # possibly add additional error checking code here, etc.

    rows_to_clear = [] # There are M rows
    cols_to_clear = [] # There are N cols
    for row in range(M):
        for col in range(N):
            if matrix[row][col] == 0:
                rows_to_clear.append(row) 
                cols_to_clear.append(col)
    #print("rows to clear: {}".format(rows_to_clear))
    #print("cols to clear: {}".format(cols_to_clear))

    for row in rows_to_clear:
        matrix[row][:] = [0 for _ in range(N)]  
    for col in cols_to_clear:
        for row in range(M):
            matrix[row][col] = 0
    return matrix


# I got it. :-)
def is_substring(s1, s2):
    return (s1 in s2) or (s2 in s1)
def is_rotation(s1, s2):
    return is_substring( s1+s1, s2)


if __name__ == "__main__":
    print("\nTesting Problem 08")
    print(is_rotation("waterbottle","erbottlewat"))
    print(is_rotation("waterbottle","erbottlewar"))

    print("\nTesting Problem 07")
    matrix = [[i for i in range(1,5)] for _ in range(3)]
    matrix[1][3] = 0
    for row in matrix:
        print(row)
    print()
    for row in clear_rows_cols(matrix):
        print(row)

    print("\nTesting Problem 06")
    N = 4
    matrix = [[i*j for i in range(N)] for j in range(N)]
    for row in matrix:
        print(row)
    print()
    for row in rotate_ninety(matrix):
        print(row)

 
    print("\nTesting Problem 05")
    print(compress("")) # (nothing)
    print(compress("a")) # a
    print(compress("aa")) # aa
    print(compress("aaa")) # a3
    print(compress("ab")) # ab
    print(compress("aabb")) # aabb
    print(compress("aabbb")) # a2b3
    print(compress("aabcccccaaa")) # a3b1c5a3

    print("\nTesting Problem 04")
    print(replace_spaces(' hi          ', 4))
    print(replace_spaces('Mr John Smith    ', 13))

    print("\nTesting Problem 03")
    print(is_permutation("asdf","fsaf"))
    print(is_permutation("asdf","fsad"))
    print(is_permutation("asdfd","fsaf"))
    print(is_permutation("nobo","boon"))

    print("\nTesting Problem 02")
    print(reverse("h"))
    print(reverse("hi"))
    print(reverse("hii"))
    print(reverse("abcdef"))

    print("\nTesting Problem 01")
    print(all_unique_nods("hi"))         # True
    print(all_unique_nods("hii"))        # False
    print(all_unique_nods("blehasdf"))   # True
    print(all_unique_nods("blehaasdf"))  # False
    print(all_unique_nods("ble haasdf")) # False
    print(all_unique_nods("blfb"))       # False
    print("")
    print(all_unique_6v1("hi"))         # True
    print(all_unique_6v1("hii"))        # False
    print(all_unique_6v1("blehasdf"))   # True
    print(all_unique_6v1("blehaasdf"))  # False
    print(all_unique_6v1("ble haasdf")) # False
    print(all_unique_6v1("blfb"))       # False
    print("")
    print(all_unique_6v2("hi"))         # True
    print(all_unique_6v2("hii"))        # False
    print(all_unique_6v2("blehasdf"))   # True
    print(all_unique_6v2("blehaasdf"))  # False
    print(all_unique_6v2("ble haasdf")) # False
    print(all_unique_6v2("blfb"))       # False
