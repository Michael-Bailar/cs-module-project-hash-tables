import math

class HashTableEntry:
    # Linked List hash table key/value pair
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, key=None, value=None):
        if value == None:
            self.head = None
        else:
            self.head = HashTableEntry(key, value)

    def add_to_head(self, key, value):
        if self.head is None:
            self.head = HashTableEntry(key, value)
        else:
            new_node = HashTableEntry(key, value)
            new_node.next = self.head
            self.head = new_node
        return self.head

    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def insert(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return current
            current = current.next
        self.add_to_head(key, value)

    def delete(self, key):
        current = self.head
        if current.key == key: #the head is to be deleted
            value = current.value
            self.head = current.next
            return value
        while current.next is not None:
            if current.next.key == key:
                #this is what we need to delete
                value = current.next.value
                current.next = current.next.next
                return value
            current = current.next
        return None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    # A hash table that with `capacity` buckets
    #that accepts string keys

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.load = 0
        for _ in range(capacity):
            self.storage.append(LinkedList(None, None))

    def get_num_slots(self):
        # Return the length of the list you're using to hold the hash
        # table data. (Not the number of items stored in the hash table,
        # but the number of slots in the main list.)

        return self.capacity

    def get_load_factor(self):
        # Return the load factor for this hash table.

        return self.load / self.capacity


    def fnv1(self, key):
        # FNV-1 Hash, 64-bit

        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash = FNV_offset_basis
        string_bytes = key.encode()

        for char in string_bytes:
            hash = hash * FNV_prime
            hash = hash ^ char
        return hash

    def hash_index(self, key):
        # Take an arbitrary key and return a valid integer index
        # between within the storage capacity of the hash table.

        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        # Store the value with the given key.
        self.load += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        index = self.hash_index(key)
        self.storage[index].insert(key, value)


    def delete(self, key):
        # Remove the value stored with the given key.
        # Print a warning if the key is not found.
        self.load -= 1
        if self.get_load_factor() < 0.25:
            self.resize(math.ceil(self.capacity/2))
        index = self.hash_index(key)
        self.storage[index].delete(key)

    def get(self, key):
        # Retrieve the value stored with the given key.
        # Returns None if the key is not found.

        index = self.hash_index(key)
        value = self.storage[index].find(key)
        #check for the key in the Linked List
    
        
        return value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # create a new array that's twice the size of the old array (capacity * 2)
        # iterate through everything and 
        # insert each one into the new array
        new_hash = HashTable(new_capacity)
        for ht in self.storage:
            current = ht.head
            while current is not None:
                new_hash.put(current.key, current.value)
                current = current.next
        self.capacity = new_hash.capacity
        self.storage = new_hash.storage
        self.load = new_hash.load



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


