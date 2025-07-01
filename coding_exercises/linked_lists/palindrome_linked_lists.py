# Implement a function to check if a linked list is a palindrome.

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

    def is_palindrome(self):
        """
        Check if the linked list is a palindrome using O(1) space.
        Uses two-pointer technique: find middle, reverse second half, compare.
        """
        if not self.head or not self.head.next:
            return True
        
        # Step 1: Find the middle using slow/fast pointers
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        second_half = self.reverse_list(slow.next)
        
        # Step 3: Compare first half with reversed second half
        first_half = self.head
        second_half_copy = second_half
        
        is_palindrome = True
        while second_half_copy:
            if first_half.data != second_half_copy.data:
                is_palindrome = False
                break
            first_half = first_half.next
            second_half_copy = second_half_copy.next
        
        # Step 4: Restore the original list (reverse back)
        slow.next = self.reverse_list(second_half)
        
        return is_palindrome

    def is_palindrome_stack(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        current = self.head
        while current:
            if current.data != stack.pop():
                return False
            current = current.next
        return True

    def is_palindrome_recursive(self):
        def is_palindrome_recursive_helper(left, right):
            if not right:
                return True
            is_pal = is_palindrome_recursive_helper(left.next, right.next)
            if not is_pal:
                return False
            return left.data == right.data and is_pal
        return is_palindrome_recursive_helper(self.head, self.head)
    
    def reverse_list(self, head):
        """Helper function to reverse a linked list"""
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
    
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
ll.append(1)
ll.print_list()
print(f"Is palindrome: {ll.is_palindrome()}")  # Should be True
print(f"Is palindrome: {ll.is_palindrome_stack()}")  # Should be True
print(f"Is palindrome: {ll.is_palindrome_recursive()}")  # Should be True

# Test case 2: Not a palindrome
ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
ll2.print_list()
print(f"Is palindrome: {ll2.is_palindrome()}")  # Should be False

# Test case 3: Even length palindrome
ll3 = LinkedList()
ll3.append(1)
ll3.append(2)
ll3.append(2)
ll3.append(1)
ll3.print_list()
print(f"Is palindrome: {ll3.is_palindrome()}")  # Should be True

# Test case 4: Single node
ll4 = LinkedList()
ll4.append(1)
ll4.print_list()
print(f"Is palindrome: {ll4.is_palindrome()}")  # Should be True

# Test case 5: Empty list
ll5 = LinkedList()
ll5.print_list()
print(f"Is palindrome: {ll5.is_palindrome()}")  # Should be True

# Complexity analysis

# SOLUTION: is_palindrome() - Two-pointer with reversal
# Time Complexity: O(n)
#   - Find middle: O(n/2) ≈ O(n)
#   - Reverse second half: O(n/2) ≈ O(n)
#   - Compare halves: O(n/2) ≈ O(n)
#   - Restore list: O(n/2) ≈ O(n)
#   - Total: O(n)
# Space Complexity: O(1)
#   - Only uses constant extra space (pointers)
#   - No additional data structures that grow with input size

# ALGORITHM EXPLANATION:
# 1. Find middle: Use slow/fast pointers to find the middle node
# 2. Reverse second half: Reverse the second half of the list
# 3. Compare: Compare first half with reversed second half
# 4. Restore: Reverse the second half back to restore original list
# 
# This approach allows us to check palindrome in O(1) space by:
# - Modifying the list structure temporarily
# - Restoring it back to original state
# - Using only constant extra space for pointers

# ALTERNATIVE APPROACHES:
# 1. Stack-based: O(n) time, O(n) space
# 2. Recursive: O(n) time, O(n) space (call stack)
# 3. Copy to array: O(n) time, O(n) space
# 
# The current approach is optimal for space complexity while maintaining
# reasonable time complexity and preserving the original list structure.
