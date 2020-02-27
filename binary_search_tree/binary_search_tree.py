import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.value.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
    
        # If target is equal to node value -> True
        # Else -> Value is not found: return false
        if self.value == target:
            return True
        else:
            return False
        
        # If target is greater than node value -> step into right node
        # Else -> Value is not found: Return false
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

        # If target is less than node value -> step into left node
        # Else -> Value is not found: return False       
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        
    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
