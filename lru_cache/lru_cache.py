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
        self.size = 0
        self.storage = {}
        self.order = DoublyLinkedList()
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
    
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
        
        # If cache is not empty
        if key in self.storage:
        
            node = self.storage[key]
            node.value = (key, value)
            # move it to end
            self.order.move_to_end(node)
            return
        
        if self.size == self.max_nodes:
            # remove oldest entry (head of linked list)
            del self.storage[self.order.head.value[0]] 
            # Delete from linked list
            self.order.remove_from_head() 
            # Resize
            self.size -= 1

        print("Adding node to list ...")
        # Add to linked list
        self.order.add_to_tail((key, value))
        # print("Problem:", self.order.tail)
        # Add to dictionary
        self.storage[key] = self.order.tail
        # Increase size
        self.size += 1


# Test Code
# cache = LRUCache()
# cache.set("item1", "a")
# cache.set("item2", "b")
# print(cache.get("item2"))

dl = DoublyLinkedList()
dl.add_to_tail(1)
print(dl.head.value)