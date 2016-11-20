
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
        print("i={}, num_ways={}".format(str(i).zfill(2), question_01(i)))
