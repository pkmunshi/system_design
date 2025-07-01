# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a-z).

def compress_string(s: str) -> str:
    if len(s) == 0:
        return ""
    
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            count = 1
    
    compressed.append(s[-1])
    compressed.append(str(count))
    
    return "".join(compressed) if len(compressed) < len(s) else s


# Optimized version that minimizes space usage
def compress_string_optimized(s: str) -> str:
    if len(s) == 0:
        return ""
    
    # First pass: Calculate compressed length
    compressed_length = 0
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_length += 1 + len(str(count))
            count = 1
    
    compressed_length += 1 + len(str(count))
    
    # If compressed string won't be shorter, return original
    if compressed_length >= len(s):
        return s
    
    # Second pass: Build compressed string
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            count = 1
    
    compressed.append(s[-1])
    compressed.append(str(count))
    
    return "".join(compressed)

print(compress_string_optimized("aabcccccaaa"))  # "a2b1c5a3"
print(compress_string_optimized("abc"))  # "abc"

# Complexity Analysis

# CURRENT SOLUTION: compress_string() function
# Time Complexity: O(n)
#   - Single loop through string: O(n)
# Space Complexity: O(n)
#   - Uses O(n) additional space for the compressed string

# OPTIMIZED SOLUTION: compress_string_optimized() function
# Time Complexity: O(n)
#   - Two passes through the string: O(n) + O(n) = O(n)
# Space Complexity: O(n) - still required for output
#   - First pass: Calculate compressed length
#   - Second pass: Build compressed string only if beneficial

# WHY O(1) SPACE IS IMPOSSIBLE:
# 1. Output Requirement: Function must return a string, which can be O(n) in length
# 2. String Immutability: Python strings are immutable, cannot modify in-place
# 3. Variable Output Size: Compressed string length depends on input pattern
#    - "aabcccccaaa" → "a2b1c5a3" (compressed)
#    - "abc" → "abc" (no compression)
# 4. Return Value: Even with in-place modification, we'd need O(n) space for the return value

# OPTIMIZATION STRATEGY:
# We can minimize space usage by:
# 1. First pass: Calculate if compression is beneficial
# 2. Second pass: Only build compressed string if it saves space
# This avoids creating unnecessary intermediate data structures
