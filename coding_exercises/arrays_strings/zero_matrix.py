# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zero_matrix(matrix):
    """
    Set entire row and column to 0 if an element is 0
    Time: O(M*N), Space: O(M+N)
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # First pass to find all rows and columns that need to be zeroed
    rows_to_zero = set()
    cols_to_zero = set()

    # Find all rows and columns that need to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
                
    # Set entire rows and columns to 0
    for row in rows_to_zero:
        for j in range(cols):
            matrix[row][j] = 0
            
    for col in cols_to_zero:
        for i in range(rows):
            matrix[i][col] = 0
            
    return matrix

def zero_matrix_in_place(matrix):
    """
    Set entire row and column to 0 if an element is 0 in place
    Time: O(M*N), Space: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Use the first row and column to store the zero information
    # Use a boolean to store if the first row and column should be zeroed
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
    
    # Check if the first row and column should be zeroed
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # Set entire rows and columns to 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # Set first row and column to 0 if needed   
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
            
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix



def print_matrix(matrix):
    """
    Print the matrix
    """
    for row in matrix:
        print(row)

# Test cases
print_matrix(zero_matrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))    
print_matrix(zero_matrix_in_place([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))    


# Complexity analysis
# Solution 1:
# Time: O(M*N), Space: O(M+N)
# where M is the number of rows and N is the number of columns
# because we are using a set to store the rows and columns that need to be zeroed
# and we are using a boolean to store if the first row and column should be zeroed
# so the total time complexity is O(M*N)
# and the space complexity is O(M+N)
# because we are using a set to store the rows and columns that need to be zeroed
# and we are using a boolean to store if the first row and column should be zeroed

# Solution 2:
# Time: O(M*N), Space: O(1)
# where M is the number of rows and N is the number of columns
# because we are using the first row and column to store the zero information
# and we are using a boolean to store if the first row and column should be zeroed
# so the total time complexity is O(M*N)
# and the space complexity is O(1)
# because we are not using any extra space

