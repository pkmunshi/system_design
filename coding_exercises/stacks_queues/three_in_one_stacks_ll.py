# TRADE-OFFS:
# 1. Speed vs Flexibility: Fast operations but fixed size
# 2. Memory vs Performance: Predictable memory usage
# 3. Simplicity vs Features: Easy to implement but limited functionality

# SOLUTION 1: FIXED ARRAY APPROACH
class ThreeInOneStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [None] * (stack_size * 3)
        self.sizes = [0] * 3

    def push(self, stack_num, value):
        if self.sizes[stack_num] >= self.stack_size:
            raise Exception("Stack is full")
        self.array[self.stack_size * stack_num + self.sizes[stack_num]] = value
        self.sizes[stack_num] += 1

    def pop(self, stack_num):
        if self.sizes[stack_num] == 0:
            raise Exception("Stack is empty")
        value = self.array[self.stack_size * stack_num + self.sizes[stack_num] - 1]
        self.array[self.stack_size * stack_num + self.sizes[stack_num] - 1] = None
        self.sizes[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        if self.sizes[stack_num] == 0:
            raise Exception("Stack is empty")
        return self.array[self.stack_size * stack_num + self.sizes[stack_num] - 1]
    
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size
    
    def print_stack(self, stack_num):
        print(f"Stack {stack_num}: {self.array[self.stack_size * stack_num:self.stack_size * (stack_num + 1)]}")



# SOLUTION 2: LINKED LIST APPROACH
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ThreeInOneStacksLinkedList:
    def __init__(self):
        # Each stack has its own head pointer
        self.heads = [None, None, None]
        self.sizes = [0, 0, 0]

    def push(self, stack_num, value):
        """Push value to specified stack using linked list"""
        new_node = Node(value)
        new_node.next = self.heads[stack_num]
        self.heads[stack_num] = new_node
        self.sizes[stack_num] += 1

    def pop(self, stack_num):
        """Pop value from specified stack"""
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        
        value = self.heads[stack_num].data
        self.heads[stack_num] = self.heads[stack_num].next
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        """Peek at top of specified stack"""
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        return self.heads[stack_num].data

    def is_empty(self, stack_num):
        return self.heads[stack_num] is None

    def get_size(self, stack_num):
        return self.sizes[stack_num]

    def print_stack(self, stack_num):
        """Print the specified stack"""
        current = self.heads[stack_num]
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Stack {stack_num}: {elements}")

# SOLUTION 3: DYNAMIC RESIZING APPROACH
class ThreeInOneStacksDynamic:
    def __init__(self, initial_size=10):
        self.initial_size = initial_size
        self.array = [None] * (initial_size * 3)
        self.sizes = [0, 0, 0]
        self.capacities = [initial_size, initial_size, initial_size]
        self.stack_starts = [0, initial_size, initial_size * 2]

    def push(self, stack_num, value):
        """Push with dynamic resizing"""
        if self.sizes[stack_num] >= self.capacities[stack_num]:
            self._resize_stack(stack_num)
        
        index = self.stack_starts[stack_num] + self.sizes[stack_num]
        self.array[index] = value
        self.sizes[stack_num] += 1

    def pop(self, stack_num):
        """Pop from specified stack"""
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        
        index = self.stack_starts[stack_num] + self.sizes[stack_num] - 1
        value = self.array[index]
        self.array[index] = None
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        """Peek at top of specified stack"""
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        index = self.stack_starts[stack_num] + self.sizes[stack_num] - 1
        return self.array[index]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] >= self.capacities[stack_num]

    def get_size(self, stack_num):
        return self.sizes[stack_num]

    def get_capacity(self, stack_num):
        return self.capacities[stack_num]

    def _resize_stack(self, stack_num):
        """Double the capacity of the specified stack"""
        old_capacity = self.capacities[stack_num]
        new_capacity = old_capacity * 2
        
        # Create new array with increased size
        new_array = [None] * (len(self.array) + old_capacity)
        
        # Copy all elements to new array
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        
        # Update array and capacities
        self.array = new_array
        self.capacities[stack_num] = new_capacity
        
        # Update stack starts for stacks after the resized one
        for i in range(stack_num + 1, 3):
            self.stack_starts[i] += old_capacity

    def print_stack(self, stack_num):
        """Print the specified stack"""
        start = self.stack_starts[stack_num]
        end = start + self.sizes[stack_num]
        elements = self.array[start:end]
        print(f"Stack {stack_num}: {elements} (size: {self.sizes[stack_num]}, capacity: {self.capacities[stack_num]})")

# TESTING ALL THREE SOLUTIONS
print("=== SOLUTION 1: FIXED ARRAY ===")
stacks1 = ThreeInOneStacks(3)
stacks1.push(0, 1)
stacks1.push(0, 2)
stacks1.push(1, 4)
stacks1.push(1, 5)
stacks1.push(2, 7)
stacks1.print_stack(0)
stacks1.print_stack(1)
stacks1.print_stack(2)

print("\n=== SOLUTION 2: LINKED LIST ===")
stacks2 = ThreeInOneStacksLinkedList()
stacks2.push(0, 1)
stacks2.push(0, 2)
stacks2.push(0, 3)
stacks2.push(1, 4)
stacks2.push(1, 5)
stacks2.push(1, 6)
stacks2.push(2, 7)
stacks2.push(2, 8)
stacks2.print_stack(0)
stacks2.print_stack(1)
stacks2.print_stack(2)

print("\n=== SOLUTION 3: DYNAMIC RESIZING ===")
stacks3 = ThreeInOneStacksDynamic(2)  # Start with small capacity
stacks3.push(0, 1)
stacks3.push(0, 2)
stacks3.push(0, 3)  # This will trigger resize
stacks3.push(0, 4)
stacks3.push(1, 5)
stacks3.push(1, 6)
stacks3.push(2, 7)
stacks3.print_stack(0)
stacks3.print_stack(1)
stacks3.print_stack(2)

# COMPLEXITY COMPARISON:

# SOLUTION 1: Fixed Array
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) where n = stack_size * 3
# Pros: Fast, simple, predictable memory usage
# Cons: Fixed size, potential waste, no flexibility

# SOLUTION 2: Linked List
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) where n = total elements across all stacks
# Pros: Dynamic size, no waste, simple implementation
# Cons: More memory overhead per element, cache-unfriendly - because we are using a linked list

# SOLUTION 3: Dynamic Resizing
# Time Complexity: O(1) amortized for push, O(1) for pop/peek
# Space Complexity: O(n) where n = total capacity across all stacks
# Pros: Dynamic size, efficient memory usage, good performance
# Cons: Complex implementation, occasional O(n) resize operations

# CHOOSING THE RIGHT SOLUTION:
# - Use Solution 1 when: Fixed size is acceptable, performance is critical
# - Use Solution 2 when: Dynamic size needed, simplicity preferred
# - Use Solution 3 when: Dynamic size needed, performance is important