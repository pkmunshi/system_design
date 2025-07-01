# Implement an algorithm in python to determine if a string has all unique characters without using any additional data structures.

def all_unique_chars(s: str) -> bool:
    """
    Return True if `s` contains no repeated characters.
    Runs in O(n²) time and O(1) extra space (only loop indices).
    Works for any Unicode string because it never assumes a fixed
    alphabet size; it simply compares characters pair-wise.
    """
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return False
    return True


def all_unique_ascii(s: str) -> bool:
    if len(s) > 256:              # cannot have all unique if more than 256 chars
        return False

    seen = 0                      # 256-bit bitset held in an int
    for ch in s:
        bit = 1 << ord(ch)        # set the bit for this character, ord() returns the unicode code point for a character
        if seen & bit:            # bit already set? duplicate!
            return False
        seen |= bit
    return True


def all_unique_lowercase(s: str) -> bool:
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if val < 0 or val > 25:
            raise ValueError("Only lowercase a-z characters allowed")
        if checker & (1 << val):
            return False
        checker |= (1 << val)
    return True


print(all_unique_chars("abc"))
print(all_unique_chars("aabc"))

print(all_unique_ascii("abc"))
print(all_unique_ascii("aabc"))

print(all_unique_lowercase("abc"))
print(all_unique_lowercase("aabc"))


# Complexity Analysis

# Solution 1: all_unique_chars() function
# Time Complexity: O(n²)
#   - Nested loops: O(n) * O(n) = O(n²)
# Space Complexity: O(1)
#   - Only uses constant space for loop indices

# Solution 2: all_unique_ascii() function
# Time Complexity: O(n)
#   - Single loop through string: O(n)
# Space Complexity: O(1)
#   - Uses constant space for the bitset
#   - No additional data structures created that grow with input size
#   - Uses O(1) additional space for the bitset

# Solution 3: all_unique_lowercase() function
# Time Complexity: O(n)
#   - Single loop through string: O(n)
# Space Complexity: O(1)
#   - Uses constant space for the bitset
#   - No additional data structures created that grow with input size
#   - Uses O(1) additional space for the bitset




