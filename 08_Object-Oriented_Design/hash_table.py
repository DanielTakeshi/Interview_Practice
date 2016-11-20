class Node:
    """ Simple, references an item and a next (nxt, not next due to python keyword). """
    def __init__(self, item, nxt=None):
        self.item = item
        self.nxt = nxt

class HashTable:
    """ 
    A Hash table which uses chaining (linked lists) to handle collisions.
    Assume that stuff we insert is an integer. If it were something else, like a
    String, then I'd change hash_code function so that it first converts the
    string to a number (e.g., ASCII code for letters, but that's a bad way to do
    things) and *then* applies the "mod" to compress it.
    """
    def __init__(self, num_buckets, load_factor=0.75, rehash_rate=2):
        self.num_keys = 0
        self.num_buckets = num_buckets
        self.buckets = [None for i in range(self.num_buckets)]
        self.load_factor = load_factor
        self.rehash_rate = rehash_rate

    def insert(self, value):
        """ Inserts using linked lists and chaining for collisions. """
        if float(self.num_keys+1)/self.num_buckets > self.load_factor:
            self.rehash()
        hash_code = self.hash_code(value)
        if self.buckets[hash_code] == None:
            self.buckets[hash_code] = Node(value)
        else:
            node = self.buckets[hash_code]
            while (node.nxt != None):
                node = node.nxt
            node.nxt = Node(value)
        self.num_keys += 1

    def insert_rehashing(self, hash_code, item, new_buckets):
        if new_buckets[hash_code] == None:
            new_buckets[hash_code] = Node(item)
        else:
            node = new_buckets[hash_code]
            while (node.nxt != None):
                node = node.nxt
            node.nxt = Node(item)

    def rehash(self):
        """ Rehashes by increasing size according to self.rehash_rate. """
        new_buckets = [None for i in range(self.num_buckets * self.rehash_rate)]
        self.num_buckets = len(new_buckets) # Put here so hash_code updates

        for old_node in self.buckets:
            if old_node == None:
                continue
            self.insert_rehashing(self.hash_code(old_node.item), old_node.item, new_buckets)
            while (old_node.nxt != None):
                old_node = old_node.nxt
                self.insert_rehashing(self.hash_code(old_node.item), old_node.item, new_buckets)
        self.buckets = new_buckets

    def hash_code(self, value):
        """ For now, use a really stupid hash function (well, compression function). """
        return value % self.num_buckets

    def pretty_print(self):
        """ For my benefit. """
        num_pad = 2
        print("")
        for b in range(self.num_buckets):
            bucket = "(b={}) [.]".format(str(b).zfill(num_pad))
            node = self.buckets[b]
            while (node != None):
                bucket += " => " +str(node.item)
                node = node.nxt
            print(bucket)

if __name__ == "__main__":
    ht = HashTable(num_buckets=4)
    ht.pretty_print()
    ht.insert(2)
    ht.insert(10)
    ht.insert(11)
    ht.pretty_print()
    print(ht.num_keys)
    print(ht.num_buckets)
    ht.insert(1)
    ht.pretty_print()
    print(ht.num_keys)
    print(ht.num_buckets)
    ht.insert(10)
    ht.insert(11)
    ht.insert(1104)
    ht.insert(1304)
    ht.pretty_print()
