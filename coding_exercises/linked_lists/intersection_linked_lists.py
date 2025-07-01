# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
# Note that the intersection is defined based on reference, not value. 
# That is, if the kth node of the first linked list is the exact same node (by reference)
#  as the jth node of the second linked list, then they are intersecting.

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


    def intersection(self, other):
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            if current1 == current2:
                return current1
            current1 = current1.next
            current2 = current2.next
        return None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll2 = LinkedList()
ll2.append(4)
ll2.append(5)
ll2.append(6)
ll2.append(3)
print(ll1.intersection(ll2))

# Complexity analysis
# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of nodes in the linked list
