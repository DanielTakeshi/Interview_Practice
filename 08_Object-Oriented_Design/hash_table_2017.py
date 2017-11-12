
class Node:
    """ Simple Node class with item and next pointers. """
    def __init__(self, k=None, v=None, n=None):
        self._key = k
        self._val = v
        self._next = n


class HashTable:
    """ 
    A Hash Table which uses chaining (with linked lists, using the `Node` class)
    to handle collisions. For simplicity, we assume that the user wants to
    insert integer items, so this avoids complications with generating
    intelligent hash functions that are specific to strings (if the user were
    hashing strings) and so forth.
    """
    def __init__(self, nbuckets=32):
        self.nbuckets = nbuckets
        self.table = [ None for _ in range(self.nbuckets) ]
        self.num_items = 0
        self.load_upper = 0.75
        self.load_lower = 0.25
        self.rescale_factor = 2.0


    def _insert(self, value, table):
        """ 
        Private method since `table` could be resized.
        """
        key = self._hash_code(value) # Not a key but a has code ...
        index = self._compress(key)
        if table[index] is None:
            # should really have a (key,value) as parameter, not just value...
            # The key here is the hash code which is NOT the key c'mon ...
            # This is implementing sets, except the value should be the key.
            table[index] = Node(k=key, v=value, n=None)
        else:
            l_node = table[index]
            while l_node._next is not None:
                l_node = l_node._next
            l_node._next = Node(k=key, v=value, n=None)


    def _compress(self, integer):
        """ 
        The compression function is technically the _last_ modulo operator. The
        hash _function_ should be done beforehand to turn the number into
        something that's ideally uniformly distributed throughout our buckets.
        Not random, obviously!  For now, `integer % 127` is like our hash fxn,
        though we could obviously just treat it as part of the compression
        function and let the hash fxn be f(i) = i, the identity.

        Update: I added a `_hash_code` function.
        """
        return (integer % 127) % self.nbuckets


    def _hash_code(self, value):
        """ assumes `value` is a string. """
        code = 0
        for char in value:
            code += (7*code + ord(char)) % 127
        return code


    def _resize(self, direction):
        """ 
        Double hash table based on load factor. 
        """
        if direction == 'increase':
            self.nbuckets *= self.rescale_factor
        elif direction == 'decrease':
            self.nbuckets /= self.rescale_factor
        else:
            raise ValueError('{} invalid'.format(direction))
        self.nbuckets = int(self.nbuckets)
        self.new_table = [ None for _ in range(self.nbuckets) ]

        for index in range(len(self.table)):
            node = self.table[index]
            while node is not None:
                self._insert(node._val, self.new_table)
                node = node._next
        self.table = self.new_table


    def insert(self, value):
        """ 
        Assumes `value` is some integer. First, resize if needed.
        Then insert the actual item into `self.table`.
        """
        self.num_items += 1
        if self.num_items / self.nbuckets > self.load_upper:
            self._resize(direction='increase') 
        self._insert(value, self.table)


    def remove(self, value):
        """ 
        Remove item and return it. Then resize if needed. For now we allow
        duplicates and just remove whichever one we find first.
        """ 
        index = self._compress( self._hash_code(value) )
        return_item = None

        if self.table[index] is not None:
            # The list exists. Return _item_, remove _node_.
            l_node = self.table[index]
            if l_node._val == value:
                return_item = value
                self.table[index] = l_node._next # Remove!
            else:
                # Check rest of list as needed
                while l_node._next is not None:
                    if l_node._next._val == value:
                        return_item = l_node._next._val
                        l_node._next = l_node._next._next
                        break
                    else:
                        l_node = l_node._next

        if return_item is not None:
            self.num_items -= 1
            if self.num_items / self.nbuckets < self.load_lower:
                self._resize(direction='decrease')

        return return_item


    def __str__(self):
        """ For my benefit. """
        string = "\nHashTable:\n"
        string += "  buckets:   {}\n".format(self.nbuckets)
        string += "  num_items: {}".format(self.num_items)
        for b in range(self.nbuckets):
            bucket = "\n(b {}) [.]".format(str(b).zfill(2))
            node = self.table[b]
            while (node != None):
                bucket += " -> (hcode={}, key={}, val=N/A)".format(node._key, node._val)
                node = node._next
            string += bucket
        return string


if __name__ == "__main__":
    ht = HashTable(nbuckets=4)

    # Note: technically, this hash table is only storing strings. It is not
    # storing key-value pairings. I kind of erred, the keys here are the
    # strings. The values should be something else. Again think of dictionaries
    # which map keys to values. So in this case the names are the keys. The
    # values should be some `definitions`.

    # For only keys, I'm basically doing sets. So it's kind of similar. :-)

    # Inserting a bunch of stuff
    print(ht)
    ht.insert("hi")
    ht.insert("daniel")
    ht.insert("daniel2")
    print(ht)
    print("\ninserting a new number which should invoke the load factor:")
    print(ht)
    ht.insert("dude")
    ht.insert("dudette")
    ht.insert("bleh")
    print(ht)
    print("\ninserting a new number which should invoke the load factor:")
    ht.insert("kthxbye")
    print(ht)
    ht.insert("jrs")
    ht.insert("shewchuk")
    print(ht)

    # Removing stuff
    print("\nNow let's remove ... nonexistent.")
    ht.remove("ben")
    print(ht)
    print("\nNow let's remove ..., which is actually in there.")
    ht.remove("bleh")
    print(ht)
    print("\nremove it again.")
    ht.remove("dudette")
    print(ht)
