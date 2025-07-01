# Write code to remove duplicates from an unsorted linked list.

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

    def remove_duplicates_with_hash_table(self):
        if not self.head:
            return
        
        seen = set()
        current = self.head
        previous = None
        
        while current:
            if current.data in seen:
                # Remove current node by updating previous.next
                previous.next = current.next
                current = current.next
            else:
                seen.add(current.data)
                previous = current
                current = current.next

    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(1)
ll.print_list() # 1 -> 2 -> 3 -> 2 -> 4 -> 1 -> None
ll.remove_duplicates()
ll.print_list() # 1 -> 2 -> 3 -> 4 -> None
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(1)
ll.remove_duplicates_with_hash_table()
ll.print_list() # 1 -> 2 -> 3 -> 4 -> None

# Complexity analysis

# SOLUTION 1: remove_duplicates() - Two-pointer approach
# Time Complexity: O(n²)
#   - Outer loop: O(n) iterations
#   - Inner loop: O(n) iterations in worst case
#   - Total: O(n) × O(n) = O(n²)
# Space Complexity: O(1)
#   - Only uses constant extra space (current, runner pointers)
#   - No additional data structures that grow with input size

# SOLUTION 2: remove_duplicates_with_hash_table() - Hash table approach
# Time Complexity: O(n)
#   - Single pass through the linked list: O(n)
#   - Hash table operations (add, contains): O(1) average case
#   - Total: O(n) × O(1) = O(n)
# Space Complexity: O(n)
#   - Hash table stores unique values seen so far
#   - In worst case, all values are unique: O(n) space
#   - In best case, all values are duplicates: O(1) space

# COMPARISON:
# - Hash table approach is faster (O(n) vs O(n²)) but uses more space
# - Two-pointer approach is slower but uses constant space
# - Hash table approach is generally preferred unless memory is extremely constrained
# - Both approaches modify the linked list in-place


