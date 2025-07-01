# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        

    def partition_with_two_lists(self, x):
        """
        Partition the linked list around value x.
        All nodes less than x come before all nodes greater than or equal to x.
        """
        if not self.head or not self.head.next:
            return
        
        # Create two dummy heads for before and after partitions
        before_head = Node(0)  # Dummy head for nodes < x
        after_head = Node(0)   # Dummy head for nodes >= x
        
        before = before_head
        after = after_head
        
        current = self.head
        
        while current:
            # Save the next node before we change current.next
            next_node = current.next
            
            if current.data < x:
                # Add to before partition
                before.next = current
                before = before.next
            else:
                # Add to after partition
                after.next = current
                after = after.next
            
            # Move to next node
            current = next_node
        
        # Connect the two partitions
        before.next = after_head.next
        after.next = None  # End the list
        
        # Update head to point to the first real node
        self.head = before_head.next

    def partition_in_place(self, x):
        """
        Alternative O(1) space solution: In-place partitioning without dummy heads.
        Moves nodes less than x to the front of the list.
        """
        if not self.head or not self.head.next:
            return
        
        # Find the first node >= x to use as pivot
        pivot = self.head
        while pivot and pivot.data < x:
            pivot = pivot.next
        
        if not pivot:
            return  # All nodes are < x, no partitioning needed
        
        # Move nodes < x to the front
        current = pivot.next
        while current:
            next_node = current.next
            
            if current.data < x:
                # Remove current from its current position
                pivot.next = current.next
                
                # Insert current at the front
                current.next = self.head
                self.head = current
            else:
                # Move pivot forward
                pivot = current
            
            current = next_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)
ll.append(4)
ll.print_list()
ll.partition_with_two_lists(5)
ll.print_list()

# Test the in-place partitioning
print("\nTesting in-place partitioning:")
ll2 = LinkedList()
ll2.append(3)
ll2.append(5)
ll2.append(8)
ll2.append(5)
ll2.append(10)
ll2.append(2)
ll2.append(1)
ll2.append(4)
ll2.print_list()
ll2.partition_in_place(5)
ll2.print_list()

# Complexity analysis

# SOLUTION 1: partition_with_two_lists() - Two-list approach
# Time Complexity: O(n) - single pass through the list
# Space Complexity: O(1) - only constant extra space (2 dummy nodes + 4 pointers)
#   - Dummy heads: 2 nodes (constant)
#   - Pointers: before, after, current, next_node (constant)
#   - No data structures that grow with input size

# SOLUTION 2: partition_in_place() - In-place approach
# Time Complexity: O(n) - two passes through the list
#   - First pass: Find pivot (O(n) worst case)
#   - Second pass: Move nodes (O(n))
# Space Complexity: O(1) - only constant extra space (3 pointers)
#   - Pointers: pivot, current, next_node (constant)
#   - No additional nodes or data structures

# COMPARISON OF O(1) SPACE SOLUTIONS:
# 1. Two-list approach (partition_with_two_lists):
#    - Pros: Single pass, maintains relative order within partitions
#    - Cons: Uses 2 dummy nodes
# 
# 2. In-place approach (partition_in_place):
#    - Pros: No dummy nodes, truly in-place
#    - Cons: Two passes, may not maintain relative order within partitions
# 
# Both solutions achieve O(1) space complexity by using only constant extra space
# regardless of the input size.