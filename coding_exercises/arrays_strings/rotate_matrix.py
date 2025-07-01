# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees.

def rotate_matrix_extra_space(matrix):
    """
    Rotate matrix by 90 degrees clockwise using extra space.
    Time: O(n²), Space: O(n²)
    """
    n = len(matrix)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    
    return rotated

def rotate_matrix_in_place(matrix):
    """
    Rotate matrix by 90 degrees clockwise in-place.
    Time: O(n²), Space: O(1)
    """
    n = len(matrix)
    
    # Rotate layer by layer, starting from outermost layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        for i in range(first, last):
            offset = i - first
            
            # Save top element
            top = matrix[first][i]
            
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Move top to right
            matrix[i][last] = top


def rotate_matrix_by_transpose_and_reverse(matrix: list[list[int]]) -> bool:
    """
    Rotate matrix by 90 degrees clockwise by transposing and reversing each row.
    Time: O(n²), Space: O(1)
    """
    n = len(matrix)

    # Step 1: Transpose (swap matrix[i][j] and matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()  # list.reverse() is O(n) time complexity for a list of length n and O(1) space complexity

    return True  # Indicating in-place success

def print_matrix(matrix):
    """Helper function to print matrix nicely"""
    for row in matrix:
        print(row)

# Test cases
matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix_5x5 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print("Original 3x3 matrix:")
print_matrix(matrix_3x3)

print("\nRotated 3x3 matrix (extra space):")
rotated_3x3 = rotate_matrix_extra_space(matrix_3x3)
print_matrix(rotated_3x3)

print("\nOriginal 4x4 matrix:")
print_matrix(matrix_4x4)

print("\nRotated 4x4 matrix (in-place):")
rotate_matrix_in_place(matrix_4x4)
print_matrix(matrix_4x4)

print("\nOriginal 5x5 matrix:")
print_matrix(matrix_5x5)

print("\nRotated 5x5 matrix (transpose and reverse):")
rotate_matrix_by_transpose_and_reverse(matrix_5x5)
print_matrix(matrix_5x5)

# COMPLEXITY ANALYSIS

# SOLUTION 1: rotate_matrix_extra_space()
# Time Complexity: O(n²)
#   - Two nested loops: O(n) × O(n) = O(n²)
#   - Each element is accessed once
# Space Complexity: O(n²)
#   - Creates a new n×n matrix
#   - Additional space proportional to input size

# SOLUTION 2: rotate_matrix_in_place()
# Time Complexity: O(n²)
#   - Outer loop: O(n/2) layers
#   - Inner loop: O(n) elements per layer
#   - Total: O(n/2) × O(n) = O(n²)
# Space Complexity: O(1)
#   - Only uses constant extra space (temp variable 'top')
#   - Modifies matrix in-place

# ALGORITHM THINKING PROCESS:

# 1. UNDERSTANDING THE ROTATION:
#   90° clockwise rotation transforms:
#   [a b c]    [g d a]
#   [d e f] →  [h e b]
#   [g h i]    [i f c]
#   
#   Pattern: (i,j) → (j, n-1-i)

# 2. EXTRA SPACE APPROACH:
#   - Create new matrix
#   - Copy elements with transformation: new[j][n-1-i] = old[i][j]
#   - Simple and straightforward

# 3. IN-PLACE APPROACH:
#   - Rotate layer by layer (like peeling an onion)
#   - For each layer, rotate 4 elements at a time
#   - Each element moves to position of next element in rotation
#   
#   For a 4×4 matrix, we have 2 layers:
#   Layer 0: corners and edges
#   Layer 1: center 2×2 (if any)

# 4. WHY IN-PLACE WORKS:
#   - Each layer can be rotated independently
#   - Within each layer, elements form a cycle
#   - We only need one temp variable to swap elements
#   - Process: top→right→bottom→left→top

# SOLUTION 3: rotate_matrix_by_transpose_and_reverse()
# Time Complexity: O(n²)
#   - Two nested loops: O(n) × O(n) = O(n²)
#   - Each element is accessed once
# Space Complexity: O(1)
#   - Only uses constant extra space
#   - Modifies matrix in-place

# 5. OPTIMIZATION INSIGHTS:
#   - In-place is more memory efficient
#   - Both approaches have same time complexity
#   - In-place is more complex but uses constant space
#   - Extra space approach is easier to understand and debug

