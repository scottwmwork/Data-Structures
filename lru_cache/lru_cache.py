import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:

    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.max_nodes = limit
        self.current = 0
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        pass

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        # Check to see if max has been reached -
        # If so, delete tail of linked list & update storage
        if self.current >= self.max_nodes:
            self.dll.tail.delete()
            self.storage.pop(key) #TODO

        self.current += 1
        # create key value variable
        key_value = {key:value}

        # add to doubly-linked-list
        self.dll.add_to_head(key_value)

        # add node to dictionary
        self.storage[key] = self.dll.head

# Test Code
cache = LRUCache()
cache.set("item1", "a")
print(cache.get("item1"))