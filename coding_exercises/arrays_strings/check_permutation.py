# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2): # length check - if not equal, not a permutation
        return False
    return sorted(s1) == sorted(s2) # sort and compare, O(n log n) time

print(is_permutation("abc", "bca"))
print(is_permutation("abc", "def"))


# O(n) time and O(n) space solution using a hash table
def is_permutation_2(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    # create a hash table for first string, O(n) time
    hash_table_1 = {}
    for char in s1:
        hash_table_1[char] = hash_table_1.get(char, 0) + 1
    
    # iterate through second string, O(n) time
    for char in s2:
        if char not in hash_table_1:
            return False
        hash_table_1[char] -= 1
        if hash_table_1[char] < 0:
            return False
    
    return True


# O(n) time and O(1) space solution using a character count array assuming ASCII (256 chars)
def is_permutation_3(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    # Assuming ASCII (256 chars)
    char_count = [0] * 256

    for ch in s1:
        char_count[ord(ch)] += 1

    for ch in s2:
        char_count[ord(ch)] -= 1
        if char_count[ord(ch)] < 0:
            return False

    return True




print(is_permutation("listen", "silent"))  # True
print(is_permutation("hello", "bello"))    # False

print(is_permutation_2("listen", "silent"))  # True
print(is_permutation_2("hello", "bello"))    # False

print(is_permutation_3("listen", "silent"))  # True
print(is_permutation_3("hello", "bello"))    # False

# Complexity Analysis

# Solution 1: is_permutation() function
# Time Complexity: O(n log n)
#   - str.sort() method has O(n log n) time complexity
#   - Comparison is O(n) time
# Space Complexity: O(n)
#   - Creates a new sorted string
#   - Uses O(n) additional space for the sorted string

# Solution 2: is_permutation_2() function
# Time Complexity: O(n)
#   - Two loops through strings: O(n) + O(n) = O(n)
# Space Complexity: O(n)
#   - Creates a hash table with O(n) space

# Solution 3: is_permutation_3() function
# Time Complexity: O(n)
#   - Two loops through strings: O(n) + O(n) = O(n)
# Space Complexity: O(1)

