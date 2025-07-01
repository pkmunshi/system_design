# Implement an algorithm to find the kth to last element of a singly linked list.

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

    def return_kth_to_last(self, k):
        if not self.head:
            return None
        current = self.head
        runner = self.head
        for _ in range(k):
            if not runner:
                return None
            runner = runner.next
        while runner:
            current = current.next
            runner = runner.next
        return current.data
    
    def return_kth_to_last_recursive(self, k):
        if not self.head:
            return None
        return self.return_kth_to_last_recursive_helper(self.head, k)
    
    def return_kth_to_last_recursive_helper(self, node, k):
        if not node:
            return 0
        index = self.return_kth_to_last_recursive_helper(node.next, k) + 1
        if index == k:
            print(f"The {k}th to last element is {node.data}")
        return index
    
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
ll.append(4)
ll.append(5)
ll.print_list()
print(ll.return_kth_to_last(2))
print(ll.return_kth_to_last_recursive(2))

# Complexity analysis
# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of nodes in the linked list
# because we are using a constant amount of extra space 

# Solution 2: return_kth_to_last_recursive() 
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of nodes in the linked list
# because we are using a recursive function to traverse the linked list
# and we are using a constant amount of extra space 

# Solution 3: return_kth_to_last_recursive_helper()
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of nodes in the linked list