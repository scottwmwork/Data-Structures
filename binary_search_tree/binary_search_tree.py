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
                    return
                else:
                    self.left.insert(value)
            elif value >= self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                    return
                else:
                    self.right.insert(value)
        else:
            self.value = value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self is None:
            return False
    
        # If target is equal to node value -> True
        # Else -> Value is not found: return false
        if self.value == target:
            return True
        
        # If target is greater than node value -> step into right node
        # Else -> Value is not found: Return false
        if target >= self.value:
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

        max = self.value
        node = self
        # Loops to right most node till node is none
        while node:
            if node.value > max:
                max = node.value
            node = node.right
        return max

    # Return the minimum value found in the tree
    def get_min(self):
        
        min = 0
        node = self
        # Loops to left most node until node is none
        while node:
            min = node.value
            node = node.left
        return min

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self is None:
            return
        else:
            cb(self.value)
            if self.left:
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # NOTE: parameter "node" is not needed or used!
        if self is None:
            print("ERROR: Empty Tree")
            return

        # Go Left
        if self.left:
            self.left.in_order_print(node = '')

        # Print main value    
        print(self.value)

        if self.right:
            if self.right.right is not None or self.right.left is not None:
                # Go Right
                self.right.in_order_print(node = '')
            else:
                print(self.right.value)
            


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        node_stack = Queue()
        print(node.value)
    
        while node.left or node.right:

            if node.left:
                print(node.left.value)
                node_stack.enqueue(node.left)

            if node.right:
                print(node.right.value)
                node_stack.enqueue(node.right)

            # Update node
            node = node_stack.dequeue()
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        node_stack = Stack()
        node_stack.push(node)
        while node:
    
            print(node.value)
            if node.left:
                node = node.left
                if node.right:
                    node_stack.push(node)
            else:
                popped_node = node_stack.pop()
                if popped_node:
                    node = popped_node.right
                else:
                    node = None
                
                
                              


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# Test Code! Delete After Finished Testing
# tree = BinarySearchTree(1)
# tree.insert(8)
# tree.insert(5)
# tree.insert(7)
# tree.insert(6)
# tree.insert(3)
# tree.insert(4)
# tree.insert(2)
# tree.dft_print(tree)