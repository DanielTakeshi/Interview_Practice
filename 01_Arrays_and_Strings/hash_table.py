"""
For practice. Do not use numpy.

Note that we don't actually use these in practice, because Python dictionaries
do the same functionality, only it's way better optimized.

Yeah, this seems to be reasonable. Still a LOT to do, but I seriously doubt it
will be anything that difficult for me.
"""

class HashTable:

    def __init__(self, size=11, ht_type="open"):
        """ Initialize the hash table. 
        
        The size is an arbitrary prime number. 
        ht_type is either "open" (open addressing with linear probing) or
        "chain" (using linked lists). Anything else is an illegal argument.
        """
        self.N = size
        self.n = 0
        if (ht_type != "open" and ht_type != "chain"):
            raise ValueError("ht_type={}, not \'open\' or \'chain\'".format(ht_type))
        self.ht_type = ht_type
        self.keys = [None]*self.N
        self.buckets = [None]*self.N


    def hash_function(self, key):
        """ Finds hash function value for key. Must be efficient!  Note: this
        also (for now) includes the compression function. So what this returns
        is an appropriate index into the hash table.
        """
        return key % self.N


    def rehash(self, old_hash):
        """ Increments old_hash by one due to linear probing. """
        return self.hash_function(old_hash+1)


    def put(self, key, data):
        """ Puts a (key,data) pairing in the hash table. We assume that if a
        duplicate key is inserted, we simply replace the value in the buckets.
        """
        hv = self.hash_function(key)

        if self.keys[hv] == None:
            self.keys[hv] = key
            self.buckets[hv] = data
            self.n += 1
            assert self.n <= self.N, \
                "Error,n={} but greater than N={}".format(self.n, self.N)
        elif self.keys[hv] == key:
            self.keys[hv] = key
            self.buckets[hv] = data
        else:
            next_hv = self.rehash(hv)
            while (self.keys[next_hv] != None and self.keys[next_hv] != key):
                next_hv = self.rehash(next_hv)
            if self.keys[next_hv] == None:
                self.keys[next_hv] = key
            self.buckets[next_hv] = data


    def print_buckets(self):
        """ A debugging method to print the hash table's buckets. """
        print("Current tables:\n")
        for b in range(self.N):
            print("{} (b={})".format(self.buckets[b], b))


if __name__ == "__main__":
    ht = HashTable()
    ht.print_buckets()
