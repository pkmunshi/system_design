# Check if one string is a rotation of another

def is_rotation(s1, s2):
    """
    Check if s1 is a rotation of s2
    """
    return len(s1) == len(s2) and s2 in s1 + s1

# Test cases
print(is_rotation("waterbottle", "erbottlewat"))  # True
print(is_rotation("waterbottle", "erbotlewatt"))  # False 

# Complexity analysis
# Concatenating two strings:
# Time Complexity: O(N + M), where N is the length of the first string and M is the length of the second string. This is because a new string is created, and the characters from both original strings must be copied into it.
# Space Complexity: O(N + M), as a new string of length N+M is created to store the result. 

# The in operator:
# Time Complexity: O(N*M), where N is the length of the longer string and M is the length of the shorter string. This is because the in operator checks each substring of length M in the longer string.
# Space Complexity: O(1), as no additional space is used.

# Overall:
# Time Complexity: O(N*M), where N is the length of the longer string and M is the length of the shorter string.
# Space Complexity: O(N + M), as a new string of length N+M is created to store the result.

