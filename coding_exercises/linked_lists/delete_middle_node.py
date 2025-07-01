# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, 
# not necessarily the exact middle) of a singly linked list, given only access to that node.

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
        
    def delete_middle_node(self, node):
        if not node or not node.next:
            return False
        node.data = node.next.data
        node.next = node.next.next
        return True
    
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
ll.print_list()
ll.delete_middle_node(ll.head.next.next)
ll.print_list()

# Complexity analysis
# Time Complexity: O(1)
# Space Complexity: O(1)
# where n is the number of nodes in the linked list
# because we are using a constant amount of extra space 
