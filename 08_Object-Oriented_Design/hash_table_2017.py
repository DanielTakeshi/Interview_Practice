class HashTable:


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
