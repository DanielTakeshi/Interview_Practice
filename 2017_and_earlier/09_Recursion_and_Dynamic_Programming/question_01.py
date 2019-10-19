
# `num_ways[i]` = number of ways to run up stairs with i steps
num_ways = [0, 1, 2, 4]

## 2017 version, recursive but w/cached values. Top-down?

def ways(n):
    if num_ways[n] != 0:
        return num_ways[n] # cached
    else:
        num_ways[n] = ways(n-3) + ways(n-2) + ways(n-1)
        return num_ways[n]

def get_num_ways(n):
    """ To avoid issues with resizing arrays. """
    assert n >= 0
    if n == 0:
        return 0
    for i in range(n-len(num_ways)+1):
        num_ways.append(0)
    return ways(n)


## 2016 version, I think bottom up? No real recursion.

def question_01(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    num_ways = [0,1,2,4] # Put 0 there to get indexing to work out
    for i in range(4,n+1):
        num_ways.append(num_ways[i-1] + num_ways[i-2] + num_ways[i-3])
    return num_ways[n]

if __name__ == "__main__":
    for i in range(38):
        print("i={}, num_ways={} and {}".format(str(i).zfill(2), question_01(i),
                get_num_ways(i)))
