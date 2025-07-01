# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

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

    def sum_lists(self, other):
        result = LinkedList()
        current1 = self.head
        current2 = other.head
        carry = 0
        while current1 or current2:
            val1 = current1.data if current1 else 0
            val2 = current2.data if current2 else 0 
            sum = val1 + val2 + carry
            result.append(sum % 10)
            carry = sum // 10
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None
        return result
    
    def sum_lists_forward(self, other):
        stack1 = []
        stack2 = []
        current1 = self.head
        current2 = other.head
        while current1:
            stack1.append(current1.data)
            current1 = current1.next
        while current2:
            stack2.append(current2.data)
            current2 = current2.next
        carry = 0
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            sum = val1 + val2 + carry
            result.append(sum % 10)
            carry = sum // 10
        return result
    
    def sum_lists_recursive(self, other):
        def sum_lists_recursive_helper(current1, current2, carry):
            if not current1 and not current2:
                return None
            val1 = current1.data if current1 else 0
            val2 = current2.data if current2 else 0
            sum = val1 + val2 + carry
            result = Node(sum % 10)
            result.next = sum_lists_recursive_helper(current1.next if current1 else None, current2.next if current2 else None, sum // 10)
            return result
        return sum_lists_recursive_helper(self.head, other.head, 0)
    
    def print_list(self):
        current = self.head
        while current:  
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll1 = LinkedList()
ll1.append(7)
ll1.append(1)
ll1.append(6)
ll2 = LinkedList()  
ll2.append(5)
ll2.append(9)
ll2.append(2)

result = ll1.sum_lists(ll2)
result.print_list()

result = ll1.sum_lists_forward(ll2)
result.print_list()

result = ll1.sum_lists_recursive(ll2)
result.print_list()

# Complexity analysis
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of nodes in the linked list

# Solution 2: sum_lists_forward()
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of nodes in the linked list

# Solution 3: sum_lists_recursive()
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of nodes in the linked list
# because we are using a recursive function to traverse the linked list
# and we are using a constant amount of extra space 

