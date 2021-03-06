class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # pseudocode
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        string_bytes = key.encode()

        hash = offset_basis

        for char in string_bytes:
            hash = hash * FNV_prime
            hash = hash ^ char
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        location = self.hash_index(key)

        if self.storage[location] != None:
                entry = self.storage[location]

                while entry:
                    if entry.key == key:
                        entry.value = value
                        break
                    elif entry.next == None:
                        entry.next = HashTableEntry(key, value)
                        break
                else:
                    entry = entry.next
        else:
            self.storage[location] = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        location = self.hash_index(key)
        entry = self.storage[location]

        if self.storage[location] == None:
            return("can't fine k and v at location")

        if entry.next == None:
            if entry.key == key:
                entry.value = None
                return
            else:
                return("no entry to delete")
        
        while entry:
            if entry.key == key:
                entry.value = None
                return(f'{key} removed')
            entry = entry.next
        return("no key found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        location = self.hash_index(key)
        entry = self.storage[location]
        item = None

        while entry:
            if entry.key == key:
                item = entry.value
                return item
            else:
                entry = entry.next
        return "can't find the value"


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head
        
        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return current

    def update_or_else_insert_at_head(self, key, value):

        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
    
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

    def update_or_else_insert_at_tail(self, key, value):
        # same as at head
        pass

    def delete(self):
        pass
