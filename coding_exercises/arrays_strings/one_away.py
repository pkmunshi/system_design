# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def is_one_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    if len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    elif len(s1) > len(s2):
        return is_one_away_insert_remove(s1, s2)
    else:
        return is_one_away_insert_remove(s2, s1)

def is_one_away_same_length(s1: str, s2: str) -> bool:
    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    return True

def is_one_away_insert_remove(s1: str, s2: str) -> bool:
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            i += 1
        else:
            i += 1
            j += 1
    return True

is_one_away("pale", "ple")  # True
is_one_away("pales", "pale")  # True
is_one_away("pale", "bale")  # True
is_one_away("paleo", "bale")  # False


# Complexity Analysis

# ALGORITHM STRATEGY:
# The algorithm uses a divide-and-conquer approach:
# 1. Quick rejection if length difference > 1 (O(1))
# 2. Route to appropriate handler based on string lengths
#    - Same length: Use replacement logic
#    - Different length: Use insert/remove logic

# MAIN FUNCTION: is_one_away()
# Time Complexity: O(n)
#   - O(1) for length difference check
#   - O(n) for the helper function call (either same_length or insert_remove)
#   - Total: O(1) + O(n) = O(n)
# Space Complexity: O(1)
#   - Only uses constant space for function calls

# HELPER FUNCTION 1: is_one_away_same_length()
# Time Complexity: O(n)
#   - Single loop through entire string length
#   - Early termination if more than 1 difference found
#   - Worst case: O(n) when strings are identical or have 1 difference
# Space Complexity: O(1)
#   - Only uses constant variables: diff_count, i

# HELPER FUNCTION 2: is_one_away_insert_remove()
# Time Complexity: O(n)
#   - Two pointers (i, j) traverse both strings
#   - Each pointer advances at most n times
#   - Early termination when mismatch is found
#   - Worst case: O(n) when strings are very similar
# Space Complexity: O(1)
#   - Only uses constant variables: i, j

# OVERALL COMPLEXITY:
# Time Complexity: O(n) where n is the length of the longer string
# Space Complexity: O(1) - constant extra space regardless of input size

# WHY THIS APPROACH IS OPTIMAL:
# 1. Early termination: Stops as soon as more than one difference is found
# 2. Single pass: Each helper function makes only one pass through the strings
# 3. Constant space: No need to store strings or create additional data structures
# 4. Handles all cases: The three edit types (insert, remove, replace) are handled efficiently
# 5. Elegant reduction: Three edit types reduced to two main cases (same length vs. different length)
