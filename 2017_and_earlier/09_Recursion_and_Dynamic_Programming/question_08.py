""" I didn't do this in 2016. """

def num_ways(n):
    if n <= 0:
        return 0
    ways = [ set(), set() ]
    ways[0].add( (0,0,0,0) )
    ways[1].add( (1,0,0,0) )

    def add_coin(tt, coin):
        assert coin in ['P', 'N', 'D', 'Q']
        if coin == 'P':
            return (tt[0]+1, tt[1], tt[2], tt[3])
        elif coin == 'N':
            return (tt[0], tt[1]+1, tt[2], tt[3])
        elif coin == 'D':
            return (tt[0], tt[1], tt[2]+1, tt[3])
        else:
            return (tt[0], tt[1], tt[2], tt[3]+1)

    # If memory is a concern, delete all sets before `n-25`.
    # Adding into a set ensures duplicates are handled.
    for i in range(2,n+1):
        new_ways = set()
        if i >= 25:
            for item in ways[i-25]:
                new_ways.add( add_coin(item, 'Q') )
        if i >= 10:
            for item in ways[i-10]:
                new_ways.add( add_coin(item, 'D'))
        if i >= 5:
            for item in ways[i-5]:
                new_ways.add( add_coin(item, 'N'))
        for item in ways[i-1]:
            new_ways.add( add_coin(item, 'P'))       
        ways.append(new_ways)

    # For completeness
    return ways


if __name__ == "__main__":
    for i in range(1,30):
        print("\n  {} cents.".format(i))
        ways = num_ways(i)
        print("  number of ways: {}".format(len(ways[-1])))
        print("(P,N,D,Q)\n")
        for way in ways[-1]:
            print(way)
